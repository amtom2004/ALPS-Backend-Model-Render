import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgis_35_sample",
        user="aron",
        password="password"
    )