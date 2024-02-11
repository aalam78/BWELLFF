from tinydb import TinyDB, Query

db = TinyDB('backend/db.json') # connect to the db file

#GET /patients
def get_patients():
    return db.all()

# use create an endpoint that diagnose problem by patient's medical record
# uses 2 endpoints:
# GET /patients/{ID} -> grab patient medical record by ID
# POST /diagnose -> diagnose the paitent's medical record with GPT 

def get_diagnosis_by_id(ID):
    patient = get_patient_by_ID(ID) # JSON of patient's medical record
    # call GPT to diagnose patient's medical record
    # return the diagnosis/more questions
    #diagnosis = 
    
    print(patient)
    return patient, 200

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
