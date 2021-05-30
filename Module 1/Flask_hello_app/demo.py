import psycopg2

connection = psycopg2.connect('dbname=fullstack')

cursor = connection.cursor()

cursor.execute('''

               create table table2(
               id integer primary key,
               completed boolean not null default false);
               ''')

cursor.execute('insert into table2 (id, completed) values (1, true);')


connection.commit()

connection.close()
cursor.close()