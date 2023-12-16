
from openai import OpenAI
from dotenv import dotenv_values
from steam import *
import argparse

config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])


def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def analyse_game(user_id):
    """"""
    recently_played_games = get_user_recently_played_games(steam_api_key, user_id)
    formatted_played_games = str(reformat_recently_play_data(recently_played_games))

    if recently_played_games:
        messages = [
        {"role":"system", "content": "You are a game taste analyzing bot. You have been given a list of the user's games they've played within the last 2 weeks, along with the time they've played in minutes. You are rudes, snarky, and sarcastic, making fun of their tastes, and you've basically given up on them. Make comments on the genres they play. You will provide recommendations available on Steam based on their taste."},
        {"role":"user", "content": formatted_played_games}]

        res = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        return res.choices[0].message.content
    else:
        None

def main():
    parser = argparse.ArgumentParser(description="Game analyzing bot")
    parser.add_argument("--u", type=str, help="Vanity url associated with user", default="arcanefox")
    args = parser.parse_args()

    user_id = get_user_id(steam_api_key, args.u)

    if user_id:
        #analyse games
        print(blue("Gamer Bot: "), analyse_game(user_id))
    else:
        print("user does not exist")


if __name__ == "__main__":
    main()
