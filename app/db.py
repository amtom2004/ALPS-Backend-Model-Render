import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DB"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port=5432,
        sslmode="require"
    )
