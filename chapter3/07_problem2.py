# . Write a program to fill in a letter template given below with name and date
# to print in 
name = ''' Dear <|Name|>,
You are selected!
<|Date|>'''


print(name.replace("<|Name|>", "kapil Joshi").replace("<|Date|>","2 febrarury,2026"))


