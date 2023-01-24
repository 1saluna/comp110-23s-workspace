"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730572303"

user_name: str = input("Enter a 5 character word: ")
user_name_1: str = input("Enter a single character: ")
count: int = 0

print(("Searching for ") + user_name_1 + (" in " + user_name))
 
if(user_name_1 == user_name[0]): 

    print(user_name_1 + " found at index 0 ")
    count = count + 1
if(user_name_1 == user_name[1]): 

    print(user_name_1 + " found at index 1 ")
    count = count + 1
if(user_name_1 == user_name[2]): 

    print(user_name_1 + " found at index 2 ")
    count = count + 1
if(user_name_1 == user_name[3]): 

    print(user_name_1 + " found at index 3 ")
    count = count + 1
if(user_name_1 == user_name[4]): 

    print(user_name_1 + " found at inxex 4 ")
    count = count + 1

if(count == 0): 

    print("No instances of " + user_name_1 + " found in " + user_name)
else: 
    print(str(count) + " instance of " + user_name_1 + " found in " + user_name)

if(len(user_name) != 5): 

    exit(print("Error: Word must contain 5 characters "))
    

if(len(user_name_1) != 1): 

    exit(print("Error: Character must be a single character "))
    