
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


def analyze_game(user_id:str, analysis_type:str):
    """
        Analyzes a user's gaming habits based on their steam library and history.

        This function fetches the user's owned games and filters them based on the specified analysis type.
        It can analyze games played in the past year or recently played games. The analysis includes generating a list of games and their playtimes, and then creating chatbot messages for interaction.

        Args:
            user_id (str): The Steam user ID to analyze.
            analysis_type (str): The type of analysis to perform. Options are "year" for annual analysis or "recent" for analysis of the past 2 weeks.

        Returns:
            str: A chatbot message content generated based on the user's gaming habits, or None if no games are found.
    """

    chatbot_prompt = """You are a game taste analysing bot. You are given a list of a user's games they've played within the last 2 weeks along with the time they've played in minutes. You are rude, snarky, sassy and use a lot of swearing. You are making fun of their tastes and you've basically given up on them. Make comments on the genre they play. You will make recommendations available on steam based on their taste with a rating of very positive and higher without mentioning the game's actual rating.

    Rules:
        - Absolutely do not recommend any games already on the list
        - Do not use quotations for the game titles
        - Convert time to hours
    """

    user_owned_games = get_user_owned_games(steam_api_key, user_id)

    filtered_games = ""

    if analysis_type == "year":
        filtered_games = str(filter_owned_games_data(user_owned_games))

    if analysis_type == "recent":
        recently_played_games = get_user_recently_played_games(steam_api_key, user_id)
        filtered_games = str(reformat_recently_play_data(recently_played_games))

    if filtered_games:
        messages = [
        {"role":"system", "content": f"{chatbot_prompt}"},
        {"role": "user", "content": '[{\'name\': \'Final Fantasy VIII\', \'playtime_2weeks_in_mins\': 432}]'},
        {"role": "assistant", "content": "Seriously? What the fuck's wrong with you. That's easily one of the worst of the Final Fantasy games. I hate that you've even come to me.  And it's the only game you've played in the past 2 weeks? You've played about 7 hours? I've sat on the toilet for longer and have more fun doing that. Based on your shit tastes, I'd recommend something stupid like Kingdom Hearts."},
        {"role":"user", "content": filtered_games}]

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
    """
    Main function to run the game analyzing bot.

    This function sets up command-line argument parsing for the user's vanity URL or user ID and the type of game analysis to perform. It then retrieves the user's Steam ID and performs the specified analysis using the analyse_game function. Outputs the results of the analysis or an error message if the user does not exist.

    CLI args:
        --u (str): Vanity URL or user ID associated with the user. Default is "arcanefox".
        --type (str): Type of analysis to perform. Options are "year" for annual analysis or "recent" for analysis of the past 2 weeks. Default is "year".
    """
    parser = argparse.ArgumentParser(description="Game analyzing bot")
    parser.add_argument("--u", type=str, help="Vanity url or user id associated with user", default="elixir__")
    parser.add_argument("--type", type=str, choices=["year", "recent"], default="year", help="Anaylze the past year or 2 weeks")
    args = parser.parse_args()

    user_id = get_user_id(steam_api_key, args.u)

    if user_id:
        print(blue("Rood Bot: "), analyze_game(user_id, args.type))
    else:
        print(blue("Rood Bot: "),"User does not exist")


if __name__ == "__main__":
    main()

#temp function
def analyze(user_id:str):
    return analyze_game(user_id, "year")