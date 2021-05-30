#SQLAlchemy Object Lifecycle

Process

Transient: Loose variable
person = Person(name = 'New Name')

Pending: Adds the variable to session
db.session.add(user)


Flush: Updates record doesnt store in database
person.query.all()

Commited: A commit leads to persisted changes on the database + lets the db.session start with a new transaction.
db.session.commit()



