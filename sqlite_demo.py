import sqlite3

conn = sqlite3.connect('employee.db')


c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

c.execute("INSERT INTO employees VALUES ('Arek', 'Zosia', 50000)")

conn.commit() 

conn.close()