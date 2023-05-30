"""
Collections of data, strings and string functions
"""

# Task 1
# Exercise: use the print statement to print
# Your name
# Your address
# Your interests
# Perform either addition or calculation with two numbers
# Use text in your addition

print("My name is Stewart.")
print("I live at 123 Fake Street, Fakesville, UK.")
print("My interests include coding, football, and astronomy.")
print(f"The sum of 1 and 1 is: {1+1}")

# There was no task 2
# Task 3: using input function
# complete the rest of the code
# Use a variable and invoke the input function to ask the user for a second number
# add the two numbers
# print out the total of the two numbers

# JS Python comparison: user input
# JS window.prompt() === Python input()
""""
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
total = first_number + second_number
print(f"The sum of the two numbers is: {total}.")
"""

# JS Python comparison: array types
# JS has array[] type, Python has more types (3) of array ("collections of data") than JS 
a_list  = [1,2,3] # (1) list, ordered
a_tuple = (1,2,3) # (2) tuple, ordered, cannot be changed (and are thus faster than lists)
a_set   = {1,2,3} # (3) set, unordered: list of unique items
# JS has object type whereas Python has dictionary type (Python dict keys must be string or number)
a_dict = {1:'apple', 2:'banana', 3:'pear'} # (4) dictionary, ordered
# Although the 4 types of array / "collections of data" in Python are declared differently, 
# the three that are ordered are all accessed via []: a_list[1], a_tuple[0], a_dict[1] 
print(f"a_list[1]: {a_list[1]}")
print(f"a_tuple[0]: {a_tuple[0]}")
print(f"a_dict[1]: {a_dict[1]}")

# Task 4 List exercise
# create a list of 6 items
# insert a new item in postion 3
# add another item to the list
# remove an item by value
# remove the item at index position 3
# for every list manipulation print the list
my_list = [1, 2, 3, 4, 5, 6]
print(f"my_list: {my_list}")
# insert a new item in position 3
my_list.insert(3, "New")
print(f"my_list (new item added): {my_list}")
# add another item to the list
my_list.append("Appended")
print(f"my_list (appending): {my_list}")
# remove an item by value
my_list.remove(5)
print(f"my_list (removed any item with value of 5 from list): {my_list}")
# remove the item at index position 3
my_list.pop(3)
print(f"my_list (popped item at position 3 off of list): {my_list}")

# Task 5: split[:] and find()
s1="I am a python programmer"
print(f"s1: {s1}")
print(f"s1[:12]: {s1[:12]}") # split results in print from index 0 to 11, output: "I am a pytho"
# JS indexOf() === Python find() 
print(f"s1.find('a'): {s1.find('a')}") # find the first occurance of "a", output: 2
print()

# Task 6: strip()
s2 = "  It is a beautiful day  "
s3 = ". Next sentence." 
print(f"s2: {s2}")
print(f"s3: {s3}")
print(f"s2.strip()+s3: {s2.strip()+s3}")   # strips away start & end white space from s2
print()

# Task 7: split(), join(), replace()
s4 = "How are you"
print(f"s4: {s4}")
print(f"split sentence '{s4}' into an array of words (split on space): {s4.split(' ')}")
print(f"join up the array of words into a sentence again, '_'.join(s4.split(' ')): {'_'.join(s4.split(' '))}")
print (f"s4.replace('How','Where'): {s4.replace('How','Where')}")
print()

# Task 8: lower(), upper(), title()
s5 = "I am your father, Luke"
print(f"s5: {s5}")
print(f"s5.lower(): {s5.lower()}")
print(f"s5.upper(): {s5.upper()}")
# JS capitialise() === Python title() 
print(f"s5.title(): {s5.title()}") # capitalize first letter of every word