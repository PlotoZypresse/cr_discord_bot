from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv('CLASH_API_KEY')
player_tag = os.getenv('PLAYER_TAG')
url = f'https://api.clashroyale.com/v1/players/{player_tag.replace("#", "%23")}'

headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    player_data = response.json()
    print(player_data)
else:
    print(f"Error: {response.status_code}")
