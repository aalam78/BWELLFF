from tinydb import TinyDB, Query
import os

#db.insert({'name': 'Jane Doe', 'age': 25}) insert a new person
#TODO: maybe add emergency contact

# # Get the directory where app.py is located
# basedir = os.path.abspath(os.path.dirname(__file__))

# # Construct the path to the 'db.json' file in the 'backend' folder
# database_path = os.path.join(basedir, '', 'db.json')

db = TinyDB('backend/db.json') # connect to the db file

def get_people():
    return db.all()

def get_person(name):
    print(name)
    return db.search(Query().name == name)

def create_person(body):
    print(body)
    db.insert(body)
    return body, 201 # 201 is the status code for successful creation

