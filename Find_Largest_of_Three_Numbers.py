x=int(input("Enter 1st number:  "))
y=int(input("Enter 2nd number:  "))
z=int(input("Enter 3rd number:  "))

if(x>y and x>z):
    print("largest number is x: ",x)
elif(y>x and y>z):
    print("largest number is y:  ",y)
else:
    print("largest number is z:  ",z)
