import random


print("""
      Rock, Paper, Sissor Game
Enter:
      0 for Rock 
      1 for Paper 
      2 for Sissor
""")
Choices = [0,1,2]
user_choice = int(input("Enter a number From Above Choices: "))
print()
if user_choice not in Choices:
    print("Invalid Input, Please enter a number between 0 and 2.")
    exit()
comp_choice = random.choice(Choices)

if user_choice == comp_choice:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("It's a Tie")
elif user_choice == 0 and comp_choice == 2:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Won")
elif user_choice == 2 and comp_choice == 0:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Lose")
elif user_choice > comp_choice:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Won")
elif user_choice < comp_choice:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Lose")

