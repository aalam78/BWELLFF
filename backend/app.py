# from flask import  render_template, Flask
# from flask_restful import Resource, Api

# from json import JSONEncoder

# import connexion

# from flask_cors import CORS, cross_origin

# # Create the application instance
# app =connexion.App(__name__, specification_dir='./') 

# app.add_api('swagger.yml') # Read the swagger.yml file to configure the endpoints

# CORS(app.app) # enable CORS

# # app.add_api("swagger.yml")
# # CORS(app)


# # @app.before_request # decorator to tell Flask to call the function before processing the request
# # def before_request(request):
# #     request.headers.add('Access-Control-Allow-Origin', '*')
# #     request.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
# #     request.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
# #     return request


# @app.route('/') # decorator to tell Flask what URL should trigger the function
# def home():
#     #A template is a file that serves as a blueprint for rendering information.
#     return render_template('home.html') # render a template

# if __name__ == '__main__':
#     host = '0.0.0.0'
#     port = 8000
    
#     #see docs
#     # localhost:8000/api/ui

#     # Run the application
#     # http://localhost:8000/api/people, will run the read_all function
#     app.run(host=host, port=port, log_level="debug") # run the application
from flask import render_template, Flask, send_from_directory
import connexion
from flask_cors import CORS

# # Create the application instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')  # Read the swagger.yml file to configure the endpoints


# enable cors with 'access control allow headers' and 'access control allow methods'
CORS(app.app, resources={r"/*": {"origins": "*"}}, headers="Content-Type", methods="GET,POST,PUT,DELETE,OPTIONS")


@app.app.route('/<path:path>')  # Notice how we access the Flask instance directly
def home(path):

    # type path and sending path to func
    return send_from_directory('../frontend/', path)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, log_level="debug")
