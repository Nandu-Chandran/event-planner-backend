from pymongo import MongoClient


client = MongoClient('localhost',27017)
db = client['EventPlanner']
event_collection= db['events']
user_collection=db['users']

users = [
    {'id': 1, 'name': 'John'},
    {'id': 2, 'name': 'Alice'},
    {'id': 3, 'name': 'Bob'},
    {'id': 4, 'name': 'Emily'},
    {'id': 5, 'name': 'David'},
]
posts= [
    {'id': 1, 'post_title': 'First Post', 'post_date': '2023-05-30', 'post_img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3lxIXAVkFS3E_NEAGTw-QH5vMWJe4_yBMDw&usqp=CAU', 'post_summary': 'This is the summary of the first post.'},
    {'id': 2, 'post_title': 'Second Post', 'post_date': '2023-05-29', 'post_img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcmkC7A-7K6-PWjzCmzFKKCczWwz4zhb9xKQ&usqp=CAU', 'post_summary': 'This is the summary of the second post.'},
    {'id': 3, 'post_title': 'Third Post', 'post_date': '2023-05-28', 'post_img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcmkC7A-7K6-PWjzCmzFKKCczWwz4zhb9xKQ&usqp=CAU', 'post_summary': 'This is the summary of the third post.'},
    {'id': 4, 'post_title': 'Fourth Post', 'post_date': '2023-05-27', 'post_img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcmkC7A-7K6-PWjzCmzFKKCczWwz4zhb9xKQ&usqp=CAU', 'post_summary': 'This is the summary of the fourth post.'},
    {'id': 5, 'post_title': 'Fifth Post', 'post_date': '2023-05-26', 'post_img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK-BTTAYyTjgBH4IjZy50ceD2IXufgGLy4bQ&usqp=CAU', 'post_summary': 'This is the summary of the fifth post.'},

]
def insert_user():
    if user_collection.count_documents({}) == 0:
        user_collection.insert_many(users)
        print("tmp users inserted")
    else:
        print("users not inserted")
def insert_post():
    if event_collection.count_documents({}) == 0:
        event_collection.insert_many(posts)
        print("tmp posts inserted")
    else:
        print("posts not inserted")

insert_user()
insert_post()
