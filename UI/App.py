from flask import Flask, render_template, request
import json
import requests

backendUri ='http://192.168.0.13:8000/'


app = Flask(__name__, template_folder="../UI/templates",
    static_folder="../static")

result=''

@app.route('/')
def Home():

    return render_template('index.html',Name='Rahul')

@app.route('/api')
def list():
     file= open("DB.txt",'r+')
     data = json.load(file)

     return data

@app.route('/login')
def home():
    return render_template("login.html")

@app.route('/signup')
def printt():
    return render_template("signup.html")

@app.route('/View')
def View():
        response = requests.get(backendUri+'api/view')
        result = response.json()
        return result

# @app.route('/input/<a>/<b>')
# def print(a,b):
#     return 'login'

@app.route('/Save',methods=['POST'])
def Post():

        data = dict(request.form)
        response = requests.post(backendUri+'api/Post',json= data)
    
        if response.status_code == 200:
            return render_template('ViewData.html')
        else:
            return f"Request failed with status: {response.status_code}"


if __name__ == '__main__':
    app.run(debug=True)