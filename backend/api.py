from tinydb import TinyDB, Query

db = TinyDB('backend/db.json') # connect to the db file

#GET /patients
def get_patients():
    return db.all()

def get_patient_by_ID(ID):
    print(ID)
    return db.search(Query().ID == ID)

#POST /patients
def create_patient_initial(body):
    print(body)
    db.insert(body)
    return body, 201 # 201 is the status code for successful creation

#PUT /patients
def update_patient(ID, body):
    print(ID)
    print(body)
    db.update(body, Query().ID == ID)
    return body, 200 # 200 is the status code for successful update
