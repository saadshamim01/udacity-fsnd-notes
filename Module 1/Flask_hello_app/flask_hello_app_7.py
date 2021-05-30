#SQLAlchemy ORM in Depth

# Terminal

# Importing
from flask_hello_app import Person, db

#Query
results = Person.query.all()

#To retrieve information like array
results[0]

#Adding Single record
person = Person(name = 'Samantha')

#Adding in session
db.session.add(person)

#Commiting changes
db.session.commit()

#Adding multiple records
person_1 = Person(name = 'Samantha')
person_2 = Person(name = 'Julius')

#Adding in session
db.session.add_all([person_1, person_2])

#Commiting changes
db.session.commit()

