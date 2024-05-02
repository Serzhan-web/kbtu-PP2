import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="Almaty250505", port=5433)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists snake(
            name VARCHAR(255),
            level INTEGER,
            score INTEGER
);
           """)
#conn.commit()
