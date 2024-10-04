from dotenv import load_dotenv
import requests
import os
import json

class ClanInfo:
    def __init__(self, clan_tag, filename=None):
        self.clan_tag = clan_tag
        self.filename = filename or f"data_{clan_tag}.json"
        self.river_race_filename = f"riverrace_{clan_tag}.json"

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
    
    def _getRiverRaceData(self):
        try:
            with open(self.river_race_filename, 'r') as file:
                data = json.load(file)
                # print("Loaded River Race Data:", data)  # Check what is being loaded
            return data
        except FileNotFoundError:
            print("River race data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON from river race data file.")
            return {}
        
    def getTag(self):
        data = self._getData()
        return data.get('tag', 'Tag not found')

    def getName(self):
        data = self._getData()
        return data.get('name', 'Name not found')
    
    def getRiverRace(self):
        load_dotenv()
        api_key = os.getenv('CLASH_API_KEY_UNI')

        # error hanfling for api key
        if not api_key:
            raise ValueError("API key is not set in environment variables.")
        
        clan_tag = self.clan_tag
        url = f'https://api.clashroyale.com/v1/clans/{clan_tag.replace("#", "%23")}/currentriverrace'

        headers = {
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            riverRaceData = response.json()
            with open(self.river_race_filename, 'w') as json_file:
                json.dump(riverRaceData, json_file, indent=2)
            print("River race data fetched and saved successfully.")
        else:
            print(f"Error: {response.status_code}")

    def deleteFile(self):
        target_file = filename or self.filename
        try:
            os.remove(target_file)
            print(f"{self.filename} has been deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")

