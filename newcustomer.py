name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
if age < 20:
    print("Minimum Age is 20")
else:
    phone = input("Enter Your Telephone Number : ")
    if phone.isnumeric() == False and len(phone) != 10:
        print("Phone Number Should be 10 Digits and Can Only Contain Numbers")
    else:
        salary = int(input("Enter Your Salary : "))
        if salary < 0:
            print("Salary Can\'t be Negative")
        else:
            print("Name : {}\nAge: {}\nPhone: {}\nSalary: {}".format(name,age,phone,salary))

def whileex():
    name = input("Enter Your Name : ")
    age = int(input("Enter Your Age : "))
    while age < 20:
        print("Age Cannot Be Lesser Than 20")
        age = input("Enter Your Age : ")
    phone = int(input("Enter Your Telephone Number : "))
    while phone.isnumeric() == False and len(phone)!= 10:
        print("Phone Number Should be 10 Digits and Can Only Contain Numbers")
        phone = input("Enter Your Telephone Number : ")
    salary = int(input("Enter Your Salary : "))
    while salary < 0:
        print("Salary Can\'t be Negative")
        salary = int(input("Enter Your Salary : "))
    print("Name : {}\nAge: {}\nPhone: {}\nSalary: {}".format(name,age,phone,salary))

a = input("Do you want to try the same again with 'WHILE LOOP'(YES/NO)?")
if a == "YES" or a == "Yes" or a=="yes":
    whileex()

    




