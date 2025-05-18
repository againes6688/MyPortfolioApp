import os
import base64
import hashlib
import requests
from flask import Flask, redirect, request, session
from flask_session import Session
from urllib.parse import urlencode
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


app = Flask(__name__)

# ======== SESSION CONFIG =========
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'  
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)  # Initialize session
# =================================

# Load LinkedIn credentials from .env
CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID')
CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET')
REDIRECT_URI = os.getenv('LINKEDIN_REDIRECT_URI')
SCOPE = 'email profile w_member_social'

def generate_code_verifier():
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8').rstrip('=')

def generate_code_challenge(code_verifier):
    digest = hashlib.sha256(code_verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')

@app.route('/')
def home():
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    state = os.urandom(16).hex()
    session['state'] = state
    session['code_verifier'] = code_verifier

    print(f"Code Verifier: {code_verifier}")
    print(f"State stored: {state}")

    auth_url = (
        'https://www.linkedin.com/oauth/v2/authorization?' +
        urlencode({
            'response_type': 'code',
            'client_id': CLIENT_ID,
            'redirect_uri': REDIRECT_URI,
            'scope': SCOPE,
            'state': state,
            'code_challenge': code_challenge,
            'code_challenge_method': 'S256',
        })
    )
    return redirect(auth_url)

@app.route('/callback')
def callback():
    session_state = session.get('state')
    received_state = request.args.get('state')
    print(f"Session state: {session_state}")
    print(f"Received state: {received_state}")

    if session_state != received_state:
        return "State mismatch. Possible CSRF attack.", 400

    auth_code = request.args.get('code')
    if not auth_code:
        return "No code received.", 400

    return exchange_code_for_token(auth_code)

def exchange_code_for_token(auth_code):
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        print(f"Access Token: {access_token}")
        return f"Access Token: {access_token}"
    else:
        print("Token request failed:", response.text)
        return f"Failed to get token: {response.text}"

# Optional: test if session works
@app.route('/test_session')
def test_session():
    session['test'] = 'hello'
    return 'Session set.'

@app.route('/get_session')
def get_session():
    return f"Test session: {session.get('test')}"
@app.route('/test_set')
def test_set():
    session['foo'] = 'bar'
    return 'Session variable set!'

@app.route('/test_get')
def test_get():
    value = session.get('foo', 'None')
    return f'Session variable is: {value}'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
