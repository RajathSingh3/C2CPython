import modulex

fname = input("Enter Your First Name : ")
lname = input("Enter Your Last Name : ")
sal = modulex.salary()
hra = modulex.hra(sal)
da = modulex.da(sal)
bonus = modulex.bonus(sal)
print("Name : ", (fname + lname))
print("Total Salary (Basic + DA + HRA + Bonus) : ", (sal+hra+da+bonus))