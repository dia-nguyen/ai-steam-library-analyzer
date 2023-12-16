import requests
from dotenv import dotenv_values

config = dotenv_values('.env')

steam_api_key = config["STEAM_API_KEY"]
user_steam_id = config["STEAM_ID"]

def get_user_info(api_key: str, user_id:str):
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {
        'key': api_key,
        'steamids': user_id,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_user_info():
    user_info = get_user_info(steam_api_key, user_steam_id)

    if user_info:
        print(user_info)
    else:
        print("Could not fetch info")

def get_owned_games(api_key: str, user_id:str):
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
    params = {
        'key': api_key,
        'steamid': user_id,
        'include_appinfo': True,
        'format': 'json'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def print_owned_games():
    owned_games = get_owned_games(steam_api_key, user_steam_id)

    if owned_games:
        print(owned_games)
    else:
        print("Could not fetch info")

print_owned_games()
