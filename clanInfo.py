from dotenv import load_dotenv
import requests
import os
import json

class ClanInfo:
    def __init__(self, clan_tag, filename):
        self.clan_tag = clan_tag
        self.filename = filename or f"data_{clan_tag}.json"

    def getClanData(self):
        load_dotenv()
        api_key = os.getenv('CLASH_API_KEY_UNI')

        # error hanfling for api key
        if not api_key:
            raise ValueError("API key is not set in environment variables.")

        clan_tag = self.clan_tag
        url = f'https://api.clashroyale.com/v1/clans/{clan_tag.replace("#", "%23")}'

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
    
    def warAttacksLeft(self):
        pass

    def deleteFile(self):
        try:
            os.remove(self.filename)
            print(f"{self.filename} has been deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")

