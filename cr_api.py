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

        # filename = f"data_{player_tag}.json"

        if response.status_code == 200:
            with open(self.filename, 'w') as json_file:
                json.dump(response.json(), json_file, indent=2)

        else:
            print(f"Error: {response.status_code}")

    def getTag(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return data.get('tag', 'Tag not found')

    def getName(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return data.get('name', 'Name not found')
        
    def deleteFile(self):
        try:
            os.remove(self.filename)
            print(f"{self.filename} has been deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")



# printData("data.json")