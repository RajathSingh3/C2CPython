a = input("Enter the Name : ")
for i in range(len(a)):
    print(a[i:i+1],"\n")

for i in a:
    print("\t",i)

print()

for i in a[::-1]:
    print("\t",i)

