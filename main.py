import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='tasks_db',
    user='tidorino',
    password='tidorino',
)
cursor = connection.cursor()
print(cursor)
connection.close()
