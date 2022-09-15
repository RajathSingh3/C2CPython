name = input("Enter the Student Name : ")
attend = int(input("Enter the Number of Days Attended : "))
totaldays = 200
if attend > 200:
    attend = input("Enter the Number of Days Attended (<=200) : ")
percent = (attend/totaldays) * 100
if percent >= 80:
    print("Dear {}, You are Eligible for the Exam".format(name))
else:
    print("Dear {}, You are not Eligible for the Exam".format(name))
