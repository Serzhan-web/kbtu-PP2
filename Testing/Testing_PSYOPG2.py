import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="lab10",
        user="postgres",
        password="Almaty250505",
        port = 5432
    )
    print("Great")
except psycopg2.Error as e:
    print("Not Great", e)