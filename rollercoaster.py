print("Welcome to Roller Coaster")
height = int(input("Enter your height: "))
if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your bill is 5 dollars")
        bill = 5
    elif age < 18:
        print("Your bill is 7 dollars")
        bill = 7
    else:
        print("Your bill is 12 dollars")
        bill = 12
    photo = input("Do you want your photo taken? Y/N: ")
    if photo == "Y":
        bill += 3
    print(f"The total bill is {bill}")
else:
    print("You are not allowed to go on a roller coaster")
#-----------------------------------------------------------------------------------------------------------
'''
Output:
Welcome to Roller Coaster
Enter your height: 121
Enter your age: 12
Your bill is 7 dollars
Do you want your photo taken? Y/N: Y
The total bill is 10
'''
