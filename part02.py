# Task 1 (if/else)
subjects = ["Math", "English", "Computers"]
print(f"Subjects:\n\t1. {subjects[0]}\n\t2. {subjects[1]}\n\t3. {subjects[2]}\n")
choice = int(input("Select a subject: "))
# if choice in range(0,3):
if choice in {0,1,2}: 
    print(f"You've input {choice} and thus selected: {subjects[choice]}")
else:
    print(f"You've input {choice} which is unfortunately not an option")

# Task 2
# Exercise: Using if Elif and else
# Create a Menu program that allows user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice
import time
menu = ["Music", "History", "Maths", "Exit"]
print(f"Subject menu:\n\t1. {menu[0]}\n\t2. {menu[1]}\n\t3. {menu[2]}\n\t4. {menu[3]}")
choice = int(input("\nPlease enter your choice: "))
if choice in {1,2,3}: 
    print(f"\nYou have selected {choice} which corresponds to: {menu[choice-1]}\n")
elif choice == 4:
    print(f"\nYou have selected {choice}... exiting the programme now... goodbye!\n")
else:
    print("\nUnknown option selected... self destructing in 3 seconds...")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("\n\n\n... BOOOOOM!\n\n\n")

# Exercise: use the arithmetic operators below inside a print statement
# plus operator +
# "use num1 and num2 variables"
# division /
# "use num3 and num4 variables"
# Floor division //
# "use num3 and num4 variables"
# Modulus %
# "use num2 and num4 variables"
num1 = 11
num2 = 22
num3 = 33
num4 = 4
print(f"num1 +  num2\t= {num1}/{num2}\t= {num1/num2}")
print(f"num3 /  num4\t= {num3}/{num4}\t= {num3/num4}")
print(f"num3 // num4\t= {num3}//{num4}\t= {num3//num4}")
print(f"num2 %  num4\t= {num2}%{num4}\t= {num2%num4}")

# 0 to 27 in steps of 3 using range function
for r in range (0,28,3):
    print(f"r={r}")
