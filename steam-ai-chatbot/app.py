import os
from flask import Flask, request, jsonify
from forms import SteamIdForm
from chatbot import *

API_SECRET_KEY = os.environ['API_SECRET_KEY']
app = Flask(__name__)

app.secret_key = API_SECRET_KEY
app.debug = True

@app.post("/analyze")
def analyze():
    data = request.get_json()
    form = SteamIdForm(data=data)

    if form.validate_on_submit():
        steam_id = form.data["steam_id"]
        bot_response = analyze_game(steam_id, "year")

        return (jsonify(status="success", message=bot_response)), 201

    else:
        return (jsonify(status="error", message="Invalid Credentials")), 400

