salary = int(input("Enter your Salary : "))
years = int(input("Enter your Tenure : "))
if years >= 10:
    salary = salary + (salary*0.15)
    print("You are Eligible for 15% Bonus, Your Salary with Bonus is : ", salary)
elif years >=5:
    salary = salary + (salary*0.10)
    print("You are Eligible for 10% Bonus, Your Salary with Bonus is : ", salary)
elif years >=3:
    salary = salary + (salary*0.05)
    print("You are Eligible for 5% Bonus, Your Salary with Bonus is : ", salary)
else:
    print("You are not Eligible for Bonus, Your Salary is : ", salary)
    