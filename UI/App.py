from flask import Flask, render_template, request
import json
import requests
import os
backendUri = os.environ.get("BACKEND_URI", "http://backend:5000/")
app = Flask(
    __name__,
    template_folder="templates",   # relative to /app
    static_folder="static",
    static_url_path="/static"
)

result = ''

@app.route('/')
def home():
    return render_template('index.html', Name='Rahul')

@app.route('/api')
def list_data():
    with open("DB.txt", 'r+') as file:
        data = json.load(file)
    return data

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/signup')
def printt():
    return render_template("signup.html")

@app.route('/View')
def view_data():
    response = requests.get(backendUri + 'api/view')
    result = response.json()
    return result

@app.route('/Authenticate', methods=['POST'])
def authenticate():
    # print('Incoming Success')
    data = dict(request.form)
    response = requests.post(backendUri + 'api/Post', json=data)
    if response.status_code == 200:
        return "Login Successful"
    else:
        return "Authentication failed"


@app.route('/Save', methods=['POST'])
def sign_up():
    try:
        data = dict(request.form)
        print("Form data:", data)

        response = requests.post(backendUri + 'api/Post', json=data)
        response.raise_for_status()  # raises exception if status != 2xx

        return render_template('ViewData.html', message="Signup successful!")

    except requests.exceptions.RequestException as e:
        print("HTTP request failed:", e)
        return f"Backend request failed: {e}", 500
    except Exception as e:
        print("Something went wrong:", e)
        return f"Internal error: {e}", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
