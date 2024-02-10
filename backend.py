from flask import Flask
from flask_restful import Resource, Api
'''
Read ->	GET	->/api/people ->	Read a collection of people.

Create ->	POST ->	-> /api/people	Create a new person.

Read ->	GET	 /api/people/<lname> ->	Read a particular person.

Update ->	PUT	/api/people/<lname> ->	Update an existing person.

Delete	-> DELETE	/api/people/<lname>	 -> Delete an existing person.

'''
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'CHATPGT ': 'DOCTOR RESPONSE'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)