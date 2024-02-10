from tinydb import TinyDB, Query

## db.update() - Update a document
## db.remove() - Remove a document
## db.search() - Query the database

# Create a new database or open an existing one
db = TinyDB('db.json')

## set up the database with test data

# Insert multiple documents at once
db.insert_multiple([
    {'name': 'Jane Doe', 'age': 25},
    {'name': 'Jim Doe', 'age': 35}
])

## Query the database
Person = Query()
results = db.search(Person.age > 30)


# Query all data
print(db.all())
