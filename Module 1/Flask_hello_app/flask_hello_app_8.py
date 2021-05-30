# Model.query Funtions

#Similar to select * from table where [...]
Person.query.filter_by(name = 'Amy')

#Similar to select * from table
Person.query.all()

#Counts number of records
Person.query.count()

#Filtering by attribute attached to the model
Person.query.filter(Person.name == 'Amy')

#Filtering across multiple models across multiple tables
Person.query.filter(Person.name == 'Amy', Team.name == 'Udacity')

#To retrieve using primary key
Person.query.get(1)

# Deleting
Product.query.filter_by(category = 'Misc').delete()

# Where chaining
Person.query.filter(Person.name == 'Amy').filter(Team.name == 'Udacity').first()

#Query using db.session, done when joining table is required
db.session.query(Person)
session.query(Person).join(Team)

#Order by
MyModel.order_by(MyModel.created_at)
MyModel.order_by(db.desc(MyModel.created_at))

#Limit
Order.query.limit(100).all()

#get() Get object by ID
model_id = 3
MyModel.query.get(model_id)

#delete() does a bulk delete operation that deletes every record matching the given query.
query = Task.query.filter_by(category='Archived')
query.delete()

#Join()
Driver.query.join('vehicles')


Implement a query to filter all users by name 'Bob'.
User.query.filter_by(name = 'Bob').all()

Implement a LIKE query to filter the users for records with a name that includes the letter "b".
User.query.filter(User.name.like('%b%')).all()

Return only the first 5 records of the query above.
User.query.Limit(5).all()

Re-implement the LIKE query using case-insensitive search.

Return the number of records of users with name 'Bob'.
 User.query.filter_by(name = 'Rob').count()
