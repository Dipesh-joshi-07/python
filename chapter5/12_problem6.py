# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique

d={}

name=input(("Enter friends name:"))
lang=input(("Enter favourite language:"))
d.update({name:lang})
name=input(("Enter friends name:"))
lang=input(("Enter favourite language:"))
d.update({name:lang})
name=input(("Enter friends name:"))
lang=input(("Enter favourite language:"))       # we dont use ""in name and lang while updating
d.update({name:lang})                           # bcz name is already string
name=input(("Enter friends name:"))
lang=input(("Enter favourite language:"))
d.update({name:lang})

print(d)