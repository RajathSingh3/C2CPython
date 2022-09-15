def totalsal(basicsal):
    hra = basicsal*0.5
    da = basicsal*0.34
    totalsalary = basicsal + hra + da
    return totalsalary

basicsal = int(input("Enter Your Basic Salary : "))
totalsalary = totalsal(basicsal)
print("TOTAL SALARY: ",totalsalary)