import os
from flask import Flask, request, jsonify
from urllib.parse import urlencode

API_SECRET_KEY = os.environ['API_SECRET_KEY']

app = Flask(__name__)

app.secret_key = API_SECRET_KEY
app.debug = True

steam_openid_url = 'https://steamcommunity.com/openid/login'

@app.route("/authentication")
def auth_with_steam():
    params = {
    'openid.ns': "http://specs.openid.net/auth/2.0",
    'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.mode': 'checkid_setup',
    'openid.return_to': 'http://127.0.0.1:5000/authorize',
    'openid.realm': 'http://127.0.0.1:5000'
    }

    query_string = urlencode(params)
    auth_url = f"{steam_openid_url}?{query_string}"
    return (jsonify(auth_url=auth_url)), 201

@app.route("/authorize")
def authorize():
    openid_identity = request.args.get("openid.claimed_id")
    if openid_identity:
        steam_id = openid_identity.split("/")[-1]
        return (jsonify(status="success", steam_id=steam_id)), 201

    else:
        return (jsonify(status="error", message="Could not successfully retrieve steam id. Please try again.")), 400

if __name__ == "__main__":
    app.run()

