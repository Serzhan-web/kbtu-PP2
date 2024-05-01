import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="Almaty250505", port=5433)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists phonebook(
            id INT PRIMARY KEY,
            username VARCHAR(255),
            phone VARCHAR(20)
);
           """)
#conn.commit()

id = int(input("Enter id: "))
username= input("Enter name: ")
phone=input("Enter phone number: ")
cur.execute(
   "INSERT INTO phonebook(id, username, phone) VALUES (%s, %s, %s)",
    (id, username, phone)
)

conn.commit()
import csv

filename = 'student.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        id,username,phone = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phonebook (id,username,phone) VALUES 
                    ({id}, '{username}', '{phone}');
        """)

        conn.commit()
#cur.execute("""DELETE FROM phonebook
#           WHERE id = 4;
#""")
#conn.commit()
# Update users name
#cur.execute("""UPDATE phonebook
 #           SET username = 'Lyailya'
#            WHERE id = 1;
#""")
#conn.commit()
#Update phones 
#cur.execute("""UPDATE phonebook
#            SET phone = '+77756496355'
#            WHERE id = 1;
#""")
#conn.commit()
#Querying data from the tables (by phone or number)
n = input("Enter name or phone:")
sql="""
        SELECT * FROM phonebook WHERE username LIKE %s OR phone LIKE %s;
    """
cur.execute(sql, (n, n))
results = cur.fetchall()
print(results)
#Implement deleting data from tables by username of phone
print("Enter the name or phone:")
delete = input()
sql="""
        DELETE FROM phonebook WHERE username = %s;
    """
cur.execute(sql, (delete,))
sql="""
        DELETE FROM phonebook WHERE phone = %s;
    """
cur.execute(sql, (delete,))
print("Contact", delete, "was deleted")