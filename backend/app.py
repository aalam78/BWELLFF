from flask import  render_template
from flask_restful import Resource, Api

from json import JSONEncoder

import connexion

from flask_cors import CORS, cross_origin

# Create the application instance
app =connexion.App(__name__, specification_dir='./') 

CORS(app.app) # enable CORS
app.add_api('swagger.yml') # Read the swagger.yml file to configure the endpoints

@app.route('/') # decorator to tell Flask what URL should trigger the function
def home():
    #A template is a file that serves as a blueprint for rendering information.
    return render_template('home.html') # render a template

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    
    #see docs
    # localhost:8000/api/ui

    # Run the application
    # http://localhost:8000/api/people, will run the read_all function
    app.run(host=host, port=port, log_level="debug") # run the application