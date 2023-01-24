"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730572303"

user_name: str = input("Enter a 5 character word: ")
count: int = 0

if(len(user_name) != 5): 
    print("Error: Word must contain 5 characters ")
    exit()

user_name_1: str = input("Enter a single character: ")

if(len(user_name_1) != 1): 
    print("Error: Character must be a single character ")
    exit(print(("Searching for ") + user_name_1 + (" in " + user_name)))
    exit( print("No instances of " + user_name_1 + " found in " + user_name))

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
    print(user_name_1 + " found at index 4 ")
    count = count + 1

if(count == 0): 
    print("No instances of " + user_name_1 + " found in " + user_name)
if(count == 1):
    print(str(count)+ " instance of " + user_name_1 + " found in " + user_name)
if(count == 2):
    print(str(count) + " instances of " + user_name_1 + " found in " + user_name)
if(count == 3):
    print(str(count) + " instances of " + user_name_1 + " found in " + user_name)
if(count == 4):
    print(str(count) + " instances of " + user_name_1 + " found in " + user_name)
    

