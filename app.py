from flask import Flask, redirect, request, g,session,url_for
from urllib.parse import urlencode
import os
from chatbot import analyze

API_SECRET_KEY = os.environ['API_SECRET_KEY']

app = Flask(__name__,
    template_folder="templates",
)

app.secret_key = API_SECRET_KEY
app.debug = True

steam_openid_url = 'https://steamcommunity.com/openid/login'

@app.before_request
def lookup_current_user():
    g.user = None
    if 'user_id' in session:
        g.user = session['user_id']


@app.route("/")
def home():
    if g.user == None:
        return '<a href="http://localhost:5001/auth">Login with steam</a>'
    else:
        return f"you're logged in {g.user}"


@app.route("/auth")
def auth_with_steam():
  params = {
    'openid.ns': "http://specs.openid.net/auth/2.0",
    'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.mode': 'checkid_setup',
    'openid.return_to': 'http://127.0.0.1:5001/success',
    'openid.realm': 'http://127.0.0.1:5001'
  }

  query_string = urlencode(params)
  auth_url = f"{steam_openid_url}?{query_string}"
  return redirect(auth_url)

#temp route
@app.route("/chat")
def get_analysis():
    user_id = session["user_id"]
    chat = analyze(user_id)

    return chat

@app.route("/success")
def success():
    openid_identity = request.args.get("openid.claimed_id")
    if openid_identity:
        steam_id = openid_identity.split("/")[-1]
        session["user_id"] = steam_id
        return redirect(url_for('home'))
    else:
        return "Authorization failed"

if __name__ == "__main__":
    app.run()

