from tinydb import TinyDB, Query

# Create a new database or open an existing one
db = TinyDB('db.json')

# Insert a new document into the database
db.insert({'name': 'John Doe', 'age': 30})

# Insert multiple documents at once
db.insert_multiple([
    {'name': 'Jane Doe', 'age': 25},
    {'name': 'Jim Doe', 'age': 35}
])

# Query the database
Person = Query()
results = db.search(Person.age > 30)

print(results)  # This will print all persons older than 30

# Update a document
db.update({'age': 31}, Person.name == 'John Doe')

# Remove a document
db.remove(Person.age < 30)

# Query all data
print(db.all())
