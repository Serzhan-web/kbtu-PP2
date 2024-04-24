import psycopg2, csv

db=psycopg2.connect(dbname='Lab10', user='postgres', password='1234', host='localhost')
current=db.cursor()

print('''What do you want?

Print "1" if you want to search contact by name or phone
Print "2" if you want to add a new contact or update existing 
Print "3" if you want to add many contacts by list
Print "4" if you want to see first N contacts
Print "5" if you want to delete contact by name or phone
Print "6" if you want to add contacts from .csv file
Print "7" if you want to change name or phone of contact
Print "8" if you want to see all names of contacts
Print "9" if you want to see all phones of contacts
Print "0" if you want to see the whole table contacts 
''')
req = input("Enter the number of request:")

if req == '1':
    n = input("Enter name or phone:")
    sql="""
        SELECT * FROM phonebook WHERE person_name LIKE %s OR phone_number LIKE %s;
    """
    current.execute(sql, (n, n))
    results = current.fetchall()
    print(results)

elif req == '2':
    name = input("Enter name:")
    phone = input("Enter phone:")
    sql="""
        DELETE FROM phonebook WHERE person_name = %s;
    """
    current.execute(sql, (name,))
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    current.execute(sql, (name, phone))

elif req == '3':
#   example of list = [('v', 123), ('xij', 1331), ('hjdh', 222425626)]
    contact = input("Enter the list of contacts:")
    
    cont = []
    for tup in contact.split('), ('):
        tup = tup.replace(')','').replace('(','')
        cont.append(tuple(tup.split(',')))
    print(cont)
    sql="""
        INSERT INTO phonebook VALUES(%s, %s);
    """
    for i in range(len(cont)):
        current.execute(sql, (cont[i][0], cont[i][1]))

elif req == '4':
    x = input("Enter the number of contacts:") 
    sql = """
        SELECT * FROM phonebook;
    """
    current.execute(sql)
    results = current.fetchmany(int(x))
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))

elif req == '5':
    print("Enter the name or phone:")
    delete = input()
    sql="""
        DELETE FROM phonebook WHERE person_name = %s;
    """
    current.execute(sql, (delete,))
    sql="""
        DELETE FROM phonebook WHERE phone_number = %s;
    """
    current.execute(sql, (delete,))
    print("Contact", delete, "has been deleted")

elif req == '6':
    sql="""
        INSERT INTO phonebook VALUES(%s, %s) returning *;
    """
    result=[]
    with open(r'C:\Users\Viktoria\Desktop\lab10\lab10\phonebook1.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            current.execute(sql, row)
            result.append(current.fetchone())
        print(result, "has been added to the phonebook")

elif req == '7':
    w = input("Do you want to update name or phone:")
    if w == 'name':
        x = input("Enter the phone_number: ")
        y = input("Enter the new name: ")
        sql = """
            UPDATE phonebook SET person_name = %s WHERE phone_number = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")
    elif w == 'phone':
        x = input("Enter the name: ")
        y = input("Enter the new phone_number: ")
        sql = """
            UPDATE phonebook SET phone_number = %s WHERE person_name = %s;
        """
        current.execute(sql, (y, x))
        print("Data has been updated")

elif req == '8':
    sql = """
        SELECT person_name FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])

elif req == '9':
    sql = """
        SELECT phone_number FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    for i in range(len(results)):
        print(results[i][0])

elif req == '0':
    sql = """
        SELECT * FROM phonebook
    """
    current.execute(sql)
    results = current.fetchall()
    print('''PHONEBOOK
=========================================
NAME                PHONE
=========================================''')
    for i in range(len(results)):
        print('{0:20}{1:20}'.format(results[i][0], results[i][1]))    

else:
    print("Request is unidentified")

current.close()
db.commit()
db.close()
