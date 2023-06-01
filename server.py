from flask import Flask
from pymongo import Mongoclient

client = Mongoclient('localhost','27017')
db=client['EventPlanner']

user_collection=client['UserDB']
event_collection=client['EventDB']


app= Flask(__name__)

@app.route('/')
def home():
    return("This is home")


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8000)
