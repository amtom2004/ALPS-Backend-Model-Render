from fastapi import APIRouter
import psycopg2

router = APIRouter()

@router.get("/db-health")
def db_health():
    try:
        conn = psycopg2.connect(
            dbname="postgis_35_sample",
            user="aron",
            password="password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        conn.close()
        return {"status": "✅ Database connected"}
    except Exception as e:
        return {"status": "❌ Database error", "details": str(e)}