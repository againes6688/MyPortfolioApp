# 🔐 LinkedIn OAuth Integration with Flask

A simple web app built with Flask that authenticates users via LinkedIn OAuth 2.0 using the **Authorization Code Flow with PKCE**, and retrieves a secure access token.

---

## 🚀 Features

- 🔐 OAuth 2.0 with PKCE (Proof Key for Code Exchange)
- 🧠 Secure session management using `Flask-Session`
- 🔒 Environment-based secret management with `.env` and `python-dotenv`
- 🧪 Debug logs to trace state and code verifier for secure auth
- 📡 API-ready for accessing LinkedIn profile, email, or posting on behalf of the user

---

## 🛠 Technologies Used

- [Python 3.11+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Session](https://pythonhosted.org/Flask-Session/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [LinkedIn Developer API](https://learn.microsoft.com/linkedin/)

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/linkedin-oauth-flask.git
cd linkedin-oauth-flask

### Create the file:

```bash
touch .env

### Open it and add the following:

LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_REDIRECT_URI=http://localhost:8080/callback

🔒 Replace the values with your actual LinkedIn Developer credentials. This file should never be committed to Git.

 Run the Flask App
```bash
python app.py

##Then open your browser and go to:

http://localhost:8080
You’ll be redirected to LinkedIn to authorize the app. If successful, you’ll get an access token printed in your terminal.
