# Write a program to create a dictionary of nepali words with values as their English
# translation. Provide user with an option to look it up

words={
    "aama":"mother",
    "baba":"father",
    "sahayag":"help",
    "basnu":"sit"
}

a=input("Enter the word:")

# print(words[a])
print(words.get(a))