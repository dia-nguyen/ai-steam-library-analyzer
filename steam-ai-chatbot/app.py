import os
from flask import Flask, request, jsonify
from forms import SteamIdForm
from flask_cors import CORS
from chatbot import *

API_SECRET_KEY = os.environ['API_SECRET_KEY']
app = Flask(__name__)

app.secret_key = API_SECRET_KEY
app.debug = True

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

@app.post("/analyze")
def analyze():
    data = request.get_json()
    form = SteamIdForm(data=data)

    if form.validate_on_submit():
        steam_id = form.data["steam_id"]
        # bot_response = analyze_game(steam_id, "year")
        sample_response = "Oh, fantastic. You're the type of person who'd probably die on a deserted island because you're too busy collecting twigs for your silly virtual house. You're a real diehard fan aren't ya? It's all the same crap, my dude. In one ear, out the other, just like the dialogue in those games. \n\nLook, it's clear you're in deep with these RPG games with all the Final Fantasy stuff going on, and you seem to have a hard-on for survival games with elements of RPG like Terraria and New World. So, here's an idea, try Divinity: Original Sin 2. It has the RPG elements you love and it's a hell of a lot better than half the stuff going on in your library. \n\nHave fun.. or not.. I don't care "

        return (jsonify(status="success", message=sample_response)), 201

    else:
        return (jsonify(status="error", message="Invalid Credentials")), 400

