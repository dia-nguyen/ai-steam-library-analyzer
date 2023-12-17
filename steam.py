import requests
from dotenv import dotenv_values
from datetime import datetime, timedelta

config = dotenv_values('.env')

steam_api_key = config["STEAM_API_KEY"]

API_URL = "https://api.steampowered.com"

def make_steam_request(api_endpoint, params):
    """
    Makes an HTTP GET request to a specified endpoint of the Steam Web API.

    This function constructs a full URL by appending the provided endpoint to the Steam API base URL.
    It then sends an HTTP GET request to that URL with the given parameters.

    Args:
        api_endpoint (str): The endpoint of the Steam API to which the request is made.
        params (dict): A dictionary of parameters to be sent with the request.

    Returns:
        dict: The JSON response from the API if the request is successful (HTTP status code 200).
        None: If the request fails or the API returns a non-200 status code.
    """
    url = f"{API_URL}/{api_endpoint}"

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_user_id(api_key:str, username:str):
    """Get user id associated with input username"""
    endpoint = "ISteamUser/ResolveVanityURL/v0001/"
    params = {
        'key': api_key,
        'vanityurl': username,
    }

    return make_steam_request(endpoint, params)["response"].get("steamid")


def get_user_info(api_key: str, user_id:str):
    """Get user info associated with user id"""

    endpoint = "ISteamUser/GetPlayerSummaries/v0002/"
    params = {
        'key': api_key,
        'steamids': user_id,
    }

    return make_steam_request(endpoint, params)


def get_user_recently_played_games(api_key: str, user_id:str):
    """Get list of recently played games by user with associated user id """

    endpoint = "IPlayerService/GetRecentlyPlayedGames/v0001/"
    params = {
        'key': api_key,
        'steamid': user_id,
        'include_appinfo': True,
        'format': 'json'
    }

    response = make_steam_request(endpoint, params)

    return response["response"].get("games") or []


def reformat_recently_play_data(recently_played_games: list):
    """ Reformats list of dictionaries to only include name of game and playtime"""
    return [{"name": game["name"], "playtime_2weeks_in_mins": game["playtime_2weeks"]} for game in recently_played_games]


def get_user_owned_games(api_key: str, user_id:str):
    """Get list of games owned by user with associated user id """

    endpoint = "IPlayerService/GetOwnedGames/v0001/"
    params = {
        'key': api_key,
        'steamid': user_id,
        'include_appinfo': True,
        'format': 'json'
    }

    response = make_steam_request(endpoint, params)

    return response["response"].get("games") or []


def filter_owned_games_data(games_list: list):
    """
    Filter list of games and return list of items with playtime over 360 mins
    TODO: check to see if we can check rtime_last_played across all requests
    """
    # one_year_ago = datetime.now() - timedelta(days=365)

    games_played_last_year = [
        game for game in games_list
        if game["playtime_forever"] > 1800
    ]

    return [{"name": game["name"], "playtime_total": game["playtime_forever"]} for game in games_played_last_year]
