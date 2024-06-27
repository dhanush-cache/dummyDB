from dbms import DBMS


class QuerySet():

    def __init__(self, dbms: DBMS) -> None:
        self.dbms = dbms
        self.CLEAN = self.drop_database()
        self.CREATE_DATABASE = self.create_database()
        self.USE_DATABASE = self.use_database()
        self.CREATE_TABLE = self.create_table()
        self.INSERT = self.insert_data()

    def drop_database(self):
        if self.dbms == DBMS.SQLITE:
            return "SELECT NULL"
        return "DROP DATABASE college"

    def create_database(self):
        if self.dbms == DBMS.SQLITE:
            return "SELECT NULL"
        return "CREATE DATABASE college"

    def use_database(self):
        if self.dbms == DBMS.SQLITE:
            return "SELECT NULL"
        return "USE college"

    def create_table(self):
        if self.dbms == DBMS.MYSQL:
            return """CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    address VARCHAR(100)
)"""

        if self.dbms == DBMS.SQL_SERVER:
            return """CREATE TABLE students (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE,
    address VARCHAR(100)
)"""

        if self.dbms == DBMS.SQLITE:
            return """CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL UNIQUE
)"""

        return "SELECT NULL"

    def insert_data(self):
        if self.dbms == DBMS.MYSQL:
            return "INSERT INTO students (name, phone, email, address) VALUES (%s, %s, %s, %s)"
        return "INSERT INTO students (name, phone, email, address) VALUES (?, ?, ?, ?)"
