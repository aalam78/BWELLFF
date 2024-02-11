import flask
from tinydb import TinyDB, Query
import requests 

import openai 
import os



openai.api_key = os.environ["OPENAI_API_KEY"]

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

db = TinyDB('backend/db.json') # connect to the db file

#GET /patients
def get_patients():
    return db.all()

# use create an endpoint that diagnose problem by patient's medical record
# uses 2 endpoints:
# GET /patients/{ID} -> grab patient medical record by ID
# POST /diagnose -> diagnose the paitent's medical record with GPT 
def get_diagnosis_by_id(body):
    ID = body.get('ID')
    prompt = body.get('prompt')
    patient = get_patient_by_ID(ID) # JSON of patient's medical record
    # call GPT to diagnose patient's medical record
    # return the diagnosis/more questions
    
    
    prompt = "Given this patient's record as this: "   + str(patient) + '. Now the patient has this question: ' + prompt + '. What is the diagnosis in 20 words or less?' 

    diagnosis = chat_with_gpt(prompt)
    print(diagnosis.response)
    return diagnosis, 200

def chat_with_gpt(prompt):
    response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=50)
    chat_response = response.choices[0].text.strip()
    return flask.jsonify({'response': chat_response})

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
