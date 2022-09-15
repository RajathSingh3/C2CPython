def salary():
    global sal
    sal = float(input("Enter the Salary : "))
    return sal

def hra(sal):
    h = sal*0.5
    return h

def da(sal):
    d = sal * 0.34
    return d

def bonus(sal):
    b = sal * 0.1
    return b
    
