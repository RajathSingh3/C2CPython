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
while len(fname) <= 0 or not fname.isalpha():
    print("Name cannot be Empty or Contain Digits!")
    fname = input("Enter Your First Name : ")
lname = input("Enter Your Last Name : ")
while len(lname) <= 0 or not lname.isalpha():
    print("Last Name cannot be Empty or Contain Digits!")
    lname = input("Enter Your Last Name : ")
phone = input("Enter Your Telephone Number : ")
while not phone.isnumeric() or len(phone) != 10:
    print("Phone Number Should Contain only 10 digits. No characters.")
    phone = input("Enter Your Telephone Number : ")
age = input("Enter Your Age : ")
while len(age) == 0 or len(age) > 3 or not age.isnumeric() or int(age)<20:
    print("Age should be above 20 and can only be Numeric. Also cannot take more than 3 digits.")
    age = input("Enter Your Age : ")
city = input("Enter your City : ")
while len(city) == 0:
    print("City name cannot be empty")
    city = input("Enter your City : ")
salary = input("Enter your salary : ")
while len(salary) == 0 or int(salary) <= 0:
    print("Salary Cannot be Empty and Can Only Accept Positive Values")
    salary = input("Enter your salary : ")
department = input("Enter Your Department : ")
while len(department) == 0:
    print("Department Name cannot be Empty")
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
