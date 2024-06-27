from dbms import DBMS
from pathlib import Path


class DBConnector():

    def __init__(self, dbms: DBMS) -> None:
        self.dbms = dbms

    def get_connection(self, **kwargs):
        if self.dbms == DBMS.MYSQL:
            from mysql.connector import connect
            conn = connect(
                host=kwargs["host"],
                username=kwargs["username"],
                password=kwargs["password"],
            )
            return conn

        if self.dbms == DBMS.SQL_SERVER:
            import pyodbc
            conn = pyodbc.connect(
                'DRIVER=' + kwargs["driver"] +
                ';SERVER=' + kwargs["server"] +
                ';Trusted_Connection=yes;'
            )
            conn.autocommit = True
            return conn

        import sqlite3
        if Path(kwargs["file"]).exists():
            Path(kwargs["file"]).unlink()
        conn = sqlite3.connect(kwargs["file"])
        return conn
