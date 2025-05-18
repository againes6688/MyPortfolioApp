

🔐 LinkedIn OAuth Integration with Flask
A simple web app built with Flask that authenticates users via LinkedIn OAuth 2.0 using the Authorization Code Flow with PKCE, and retrieves a secure access token.

🚀 Features
🔐 OAuth 2.0 with PKCE (Proof Key for Code Exchange)

🧠 Secure session management using Flask-Session

🔒 Environment-based secret management with .env and python-dotenv

🧪 Debug logs to trace state and code verifier for secure auth

📡 API-ready for accessing LinkedIn profile, email, or posting on behalf of the user

🛠 Technologies Used
Python 3.11+

Flask

Flask-Session

python-dotenv

LinkedIn Developer API

🧰 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/linkedin-oauth-flask.git
cd linkedin-oauth-flask
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env File
bash
Copy
Edit
touch .env
Add the following to .env:

env
Copy
Edit
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_REDIRECT_URI=http://localhost:8080/callback
⚠️ Never share this file publicly. It is ignored by .gitignore.

4. Run the Flask App
bash
Copy
Edit
python app.py
Visit http://localhost:8080 in your browser. You will be redirected to LinkedIn to authenticate.

📂 Folder Structure
bash
Copy
Edit
linkedin-oauth-flask/
│
├── app.py                  # Main Flask app
├── .env                   # Environment variables (not tracked by Git)
├── .gitignore             # Ignore .env and session files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
💬 What You Can Do With This
Authenticate users through LinkedIn

Retrieve profile info or email via LinkedIn APIs

Post content to a user's LinkedIn feed (with additional permissions)

Use this as a portfolio project or base for a full LinkedIn-integrated app

🛡 Security Notes
Sessions are stored server-side (filesystem) for safety.

API secrets are managed through .env and not exposed in code.

The PKCE method prevents authorization code interception.
