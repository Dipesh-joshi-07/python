# if elif else ladder

a=int(input("Enter your age :"))

if(a>16):
    print("you are eligible for vote")

elif(a<0):
    print("you are entering wrong data.")

elif(a==0):
    print("you are entering 0 which is not possible.")


else:
     print("you are not eligible for vote")
