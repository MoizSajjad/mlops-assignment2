# backend/wait_for_db.py
import time
import psycopg2
from psycopg2 import OperationalError

while True:
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="database",
            port="5432"
        )
        conn.close()
        print("Database is ready!")
        break
    except OperationalError:
        print("Waiting for database...")
        time.sleep(2)
