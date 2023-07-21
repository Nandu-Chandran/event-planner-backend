from flask import Flask, jsonify,make_response,request
from pymongo import MongoClient
from bson import json_util
import json
from flask_cors import CORS
from jsonschema import validate

client = MongoClient('localhost',27017)
db=client['EventPlanner']

user_collection=db['users']
event_collection=db['events']


app= Flask(__name__)
cors=CORS(app)

event_schema={
    "type": "object",
    "properties": {
        "start_date": {"type": "string", "format": "date"},
        "end_date": {"type": "string", "format": "date"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "author": {"type": "string"},
    },
    "required": ["start_date", "end_date", "title"]
}


@app.route('/events',methods=['GET'])
def get_events():
    events = list(event_collection.find({},{'_id':0,'id':1,'post_title':1,'post_date':1,'post_summary':1,'post_img':1}))
    print(events)
    return jsonify(events)

@app.route('/events',methods=['POST'])
def post_events():
    data= request.get_json()
    try:
        validate(instance=data, schema=event_schema)
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({'error': 'Invalid event data', 'details': str(e)}), 400
    #print(data)
    update = event_collection.insert_one(data)
    return (jsonify('success')),201

# @app.route('/sign-up', method=['GET'])
# def sign_up():
#     pass

# @app.route('/login', method=['GET'])
# def login():
#     pass

# @app.route('/login', method=['GET'])
# def logout():
#     pass

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8000)


# @app.route('/events',methods=['POST'])
# def add_events():
#     events = list(event_collection)
