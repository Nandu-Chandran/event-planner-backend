from flask import Flask
from pymongo import MongoClient

client = MongoClient('localhost','27017')
db=client['EventPlanner']

user_collection=db['users']
event_collection=db['events']


app= Flask(__name__)

@app.route('/events',methods=['GET'])
def home():
    return("This is home")


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8000)
