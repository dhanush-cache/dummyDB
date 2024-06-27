from data_gen import get_person
from connections import DBConnector
from dbms import DBMS
from queries import QuerySet

dbms = DBMS.SQLITE
entries = 10

mysql = {
    "host": "localhost",
    "username": "root",
    "password": "1234"
}

sqlserver = {
    "server": r"DESKTOP-G2IOM67\SQLEXPRESS",
    "driver": "{ODBC Driver 17 for SQL Server}"
}

sqlite = {
    "file": "db.sqlite3"
}

conn = DBConnector(dbms).get_connection(**sqlite)

queries = QuerySet(dbms)

cursor = conn.cursor()

try:
    cursor.execute(queries.CLEAN)
finally:
    cursor.execute(queries.CREATE_DATABASE)
    cursor.execute(queries.USE_DATABASE)

cursor.execute(queries.CREATE_TABLE)

for i in range(entries):
    print(f"Inserting row: {i + 1}")

    person = get_person()
    name = person["name"]
    phone = person["phone"]
    email = person["email"]
    address = person["address"]

    values = (name, phone, email, address)
    cursor.execute(queries.INSERT, values)


cursor.close()
conn.commit()
conn.close()
