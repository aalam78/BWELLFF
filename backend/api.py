from tinydb import TinyDB, Query

#db.insert({'name': 'Jane Doe', 'age': 25}) insert a new person
#TODO: maybe add emergency contact

db = TinyDB('db.json') # connect to the db file

def get_people():
    return db.all()

def get_person(name):
    print(name)
    return db.search(Query().name == name)

def create_person(body):
    print(body)
    db.insert(body)
    return body, 201 # 201 is the status code for successful creation