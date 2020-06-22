import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'Arnob' user = 'postgres' password = 'arnob1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity, price):
    conn = psycopg2.connect("dbname = 'Arnob' user = 'postgres' password = 'arnob1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    create_table()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname = 'Arnob' user = 'postgres' password = 'arnob1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'Arnob' user = 'postgres' password = 'arnob1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item =%s",(item,))
    conn.commit()
    conn.close()



def update(price, quantity,item):
    conn = psycopg2.connect("dbname = 'Arnob' user = 'postgres' password = 'arnob1234' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET price=%s, quantity =%s WHERE item = %s",(price, quantity,item))
    conn.commit()
    conn.close()
create_table()
# insert('Mango', 20, 12)
delete("Mango")
update(12.5, 10, "Apple")
print(view())
