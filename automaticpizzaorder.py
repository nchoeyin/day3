print("Welcome to Pizza World!")
size = input("Enter S for small or M for Medium or L for Large: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
add_pepperoni = input("Do you  want a pepparoni? Y/N ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want an extra cheese? Y/N ")
if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is : {bill}")
'''
------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
Welcome to Pizza World!
Enter S for small or M for Medium or L for Large: L
Do you  want a pepparoni? Y/NY
Do you want an extra cheese? Y/NN
Your total bill is : 28

Welcome to Pizza World!
Enter S for small or M for Medium or L for Large: S
Do you  want a pepparoni? Y/N N
Do you want an extra cheese? Y/N N
Your total bill is : 15

Welcome to Pizza World!
Enter S for small or M for Medium or L for Large: M
Do you  want a pepparoni? Y/N Y
Do you want an extra cheese? Y/N Y
Your total bill is : 24
------------------------------------------------------------------------------------------------------------------------------------------------------
'''
