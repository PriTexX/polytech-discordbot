import psycopg2

from config import *


class AbstractDAO:

    def __init__(self):
        pass

    def __enter__(self):
        self._connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE)
        print(self._connection.get_dsn_parameters(), "\n")
        return self

    def __exit__(self, type, value, traceback):
        self._connection.close()

    def _select_one(self, query: str, params: tuple = None):
        cursor = self._connection.cursor()
        cursor.execute(query, params)
        record = cursor.fetchone()
        cursor.close()
        return record

    def _select_many(self, query: str, params: tuple = None):
        cursor = self._connection.cursor()
        cursor.execute(query, params)
        record = cursor.fetchall()
        cursor.close()
        return record

    def _execute(self, query: str, params: tuple = None):
        cursor = self._connection.cursor()
        cursor.execute(query, params)
        self._connection.commit()
        rows = cursor.rowcount
        cursor.close()
        return rows
