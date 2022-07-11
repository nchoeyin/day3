print("Welcome to the love calculator")
his_name = input("Enter the man's name: ")
her_name = input("Enter the woman's name: ")
his = his_name.lower().strip()
her = her_name.lower().strip()
both_names = his+her
print(both_names)
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")
print(f" t occurs {t} times")
print(f" r occurs {r} times")
print(f" u occurs {u} times")
print(f" e occurs {e} times")
true = t+r+u+e
print(f" Total : {true}")

print(f" l occurs {l} times")
print(f" o occurs {o} times")
print(f" v occurs {v} times")
print(f" e occurs {e} times")
love = l+o+v+e
print(f" Total : {love}")


score = str(true)+str(love)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score>= 40 and score <=50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------
Output:
1.
Welcome to the love calculator
Enter the man's name: Kanye West
Enter the woman's name: Kim kardashian
kanye westkim kardashian
 t occurs 1 times
 r occurs 1 times
 u occurs 0 times
 e occurs 2 times
 Total : 4
 l occurs 0 times
 o occurs 0 times
 v occurs 0 times
 e occurs 2 times
 Total : 2
Your score is 42, you are alright together

2.
Welcome to the love calculator
Enter the man's name: adam
Enter the woman's name: eve
adameve
 t occurs 0 times
 r occurs 0 times
 u occurs 0 times
 e occurs 2 times
 Total : 2
 l occurs 0 times
 o occurs 0 times
 v occurs 1 times
 e occurs 2 times
 Total : 3
Your score is 23
---------------------------------------------------------------------------------------------------------------------------------------------------------
'''





