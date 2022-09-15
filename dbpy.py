import mariadb
import sys
conn = mariadb.connect(
    user = "root",
    password = "root",
    host = "localhost",
    port = 3306,
    database = "employee"
)
fname = input("Enter Your First Name : ")
lname = input("Enter Your Last Name : ")
phone = input("Enter Your Telephone Number : ")
age = input("Enter Your Age : ")
city = input("Enter your City : ")
salary = input("Enter your salary : ")
department = input("Enter Your Department : ")
cur = conn.cursor()
conn.autocommit = True
try:
    cur.execute("create table customer(fname varchar(255) NOT NULL,lname varchar(255) NOT NULL, phone int,age int,city varchar(255),salary float,department varchar(255));")
except Exception as y:
    print(y)
insertquery = "insert into customer (fname, lname, phone, age, city, salary, department)values(%s, %s, %s, %s, %s, %s, %s)"
data = [fname, lname, phone, age, city, salary, department]
cur.execute(insertquery, data)
cur.execute("select fname, phone, age, salary from customer;")
for (fname, phone, age, salary) in cur:
    print("Name: ", {fname}, "Age : ", {phone}, "Age : ", {age}, "Salary : ", {salary})
