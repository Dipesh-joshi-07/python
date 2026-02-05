# write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.


m1=int(input("Enter subject 1 marks:"))
m2=int(input("Enter subject 2 marks:"))
m3=int(input("Enter subject 3 marks:"))

# check for total percent

total_percentage =(m1+m2+m3)/3

if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass. " " your total percen" ,total_percentage)
else:
    print("You are fail.try next time:",total_percentage)