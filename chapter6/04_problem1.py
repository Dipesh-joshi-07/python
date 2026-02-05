# . Write a program to find the greatest of four numbers entered by the user.

a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))
d=int(input("enter num4:"))

if(a>b and a>c and a>d):
    print("greatest number is a:",a)

elif(b>c and b>a and b>d):
    print("greatest number is b:",b)

elif(c>a and c>b and c>d):
    print("greatest number is c:",c)

else:
    print("greatest number is d:",d)
