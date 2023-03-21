import sqlite3


conn = sqlite3.connect("demo2.sqlite3")
cursor = conn.cursor()

print("Database conected")
conn.execute("update school set marks=60 where id=2")
conn.commit()

# display record after the delete

for i in cursor.execute("select id, Name, age, address, marks from school"):
    print("id=",i[0])
    print("Name=",i[1])
    print("age=",i[2])
    print("address=",i[3])
    print("marks=",i[4], '\n')

conn.commit()
conn.close()

