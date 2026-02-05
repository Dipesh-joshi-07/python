# multiple if
# both are independent statement.if statement can be alone used

a=int(input("Enter your age :"))

#if statement 1
if(a%2==0):
    print("number is even")
#end of statement no 1

#if statement 2
if(a>=16):
    print("you are eligible for vote")

elif(a<0):
    print("you are entering wrong data.")

elif(a==0):
    print("you are entering 0 which is not possible.")


else:
     print("you are not eligible for vote")
#end of statement no 2