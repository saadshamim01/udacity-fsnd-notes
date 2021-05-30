import psycopg2

connection = psycopg2.connect('dbname=fullstack')

cursor = connection.cursor()

cursor.execute('Drop table if exists table2;')


cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('insert into table2 (id, completed) values (%s, %s);', (1, True))


SQL = 'insert into table2 (id, completed) values (%(id)s, %(completed)s);'

data = {
    'id' : 2,
    'completed' : False
}

cursor.execute('insert into table2 (id, completed) values (%s, %s);', (3, True))


cursor.execute(SQL, data)

cursor.execute('select * from table2;')

result = cursor.fetchall()
print('fetchall',result)

result2 = cursor.fetchone()
print('fetchone', result2)

result3 = cursor.fetchmany(2)
print('fetcchmany',result)

connection.commit()

connection.close()
cursor.close()