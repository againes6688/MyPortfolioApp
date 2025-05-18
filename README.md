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
