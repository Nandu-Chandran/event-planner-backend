from flask import Flask, jsonify,make_response
from pymongo import MongoClient
from bson import json_util
import json
from flask_cors import CORS


client = MongoClient('localhost',27017)
db=client['EventPlanner']

user_collection=db['users']
event_collection=db['events']


app= Flask(__name__)
cors=CORS(app)

@app.route('/events',methods=['GET'])
def get_events():
    events = list(event_collection.find({},{'_id':0,'id':1,'post_title':1,'post_date':1,'post_summary':1,'post_img':1}))
    print(events)
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8000)


# @app.route('/events',methods=['POST'])
# def add_events():
#     events = list(event_collection)