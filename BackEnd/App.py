from urllib.parse import quote_plus
from flask import Flask, jsonify, request
import pymongo
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
# Encode username and password
username = quote_plus("rahul")  # encode special chars if any
password = quote_plus("qZKESVJVzfbD9XFp")

# Use f-string to inject username and password
uri = f"mongodb+srv://{username}:{password}@rahul.odnudlr.mongodb.net/?retryWrites=true&w=majority"

#Get from Env varibale
load_dotenv()

uri2 = os.getenv('uri2')

# Connect to MongoDB
client = pymongo.MongoClient(uri2, server_api=ServerApi('1'))

# Ping to check connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
    exit(1)

# Select database and collection
db = client.test  # you can change 'test' to your database name
coll = db['Rahul']

# Flask app
app = Flask(__name__)

@app.route('/')
def Home():
    return "Welcome To Backend API Project"

@app.route('/api/Post', methods=['POST'])
def Save():
    print('Incoming Success')
    userData = dict(request.json)

    coll.insert_one(userData)
    return "Data submitted successfully"

@app.route('/api/view')
def Get():
    
    return jsonify(list(coll.find({}, {'_id': 0})))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
