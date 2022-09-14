a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
if a > b and a > c:
    print("The Greatest Number is A : ",a)
elif b>a and b>c:
    print("The Greatest Number is B : ",b)
else:
    print("The Greatest Number is C : ",c)