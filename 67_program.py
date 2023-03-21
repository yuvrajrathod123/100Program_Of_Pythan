
import sqlite3

conn = sqlite3.connect("demo2.sqlite3")
cursor = conn.cursor()

print("Database conected")

# creating the table

cursor.execute("create table school(id INT, Name TEXT, age INT, address char(50), marks INT); ")

# inserting the data

cursor.execute("insert into school(id, Name, age, address, marks) VALUES (1,'Yuvraj',20,'mumbai',95);")

cursor.execute("insert into school(id, Name, age, address, marks) VALUES (2,'Mayur',20,'Aurangabad',95);")

cursor.execute("insert into school(id, Name, age, address, marks) VALUES (3,'Mayur',20,'Aurangabad',95);")

# displaying thhe data

for i in cursor.execute("select id, Name, age, address, marks from school"):
    print("id=",i[0])
    print("Name=",i[1])
    print("age=",i[2])
    print("address=",i[3])
    print("marks=",i[4], '\n')

cursor.close
conn.commit()
conn.close()


