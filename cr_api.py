from dotenv import load_dotenv
import requests
import os
import json



class PlayerInfo:
    def __init__(self, player_tag, filename):
        self.player_tag = player_tag
        self.filename = filename or f"data_{player_tag}.json"

    def getPlayerData(self):
        load_dotenv()
        api_key = os.getenv('CLASH_API_KEY')

        # error hanfling for api key
        if not api_key:
            raise ValueError("API key is not set in environment variables.")

        player_tag = self.player_tag
        url = f'https://api.clashroyale.com/v1/players/{player_tag.replace("#", "%23")}'

        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(self.filename, 'w') as json_file:
                json.dump(response.json(), json_file, indent=2)

        else:
            print(f"Error: {response.status_code}")

    def _getData(self):
         with open(self.filename, 'r') as file:
             return json.load(file)

    def getTag(self):
        data = self._getData()
        return data.get('tag', 'Tag not found')

    def getName(self):
        data = self._getData()
        return data.get('name', 'Name not found')
    
    def playerWinRate(self):
        data = self._getData()
        wins = int(data.get('wins'))
        totalGames = int(data.get('battleCount'))
        winRate = wins/totalGames
        return f'All Time winrate: {winRate:.2f}'
        
    def clanInfo(self):
        data = self._getData()
        clan_info = data.get('clan', {})
        tag = clan_info.get('tag', 'Tag not found')
        name = clan_info.get('name', 'Name not found')
        return f'\n\tClan tag: {tag}, \n\tClan name: {name}'
        
    def deleteFile(self):
        try:
            os.remove(self.filename)
            print(f"{self.filename} has been deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")
