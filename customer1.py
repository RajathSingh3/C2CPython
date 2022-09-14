name = input("Enter Your First Name : ")
while len(name) <= 0 or not name.isalpha():
    print("Name cannot be Empty or Contain Digits!")
    name = input("Enter Your First Name : ")
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
print()
print("Name : {}\nPhone: {}\nAge: {}\nSalary: {}\nDepartment: {}".format((name + " " + lname), phone, age, salary, department))
    

