import random

print()
print("""
      Rock, Paper, Sissor Game
Enter:
      Rock 
      Paper 
      Sissor
""")


Choices = ["rock","paper","scissor"]
user_choice = input("Enter your choices: ")
user_choice = user_choice.lower()
print()
if user_choice not in Choices:
    print("Invalid Input")
    exit()
comp_choice = random.choice(Choices)

# Seven possible cases, one for tie and six for others.

if user_choice == comp_choice:
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("It's a Tie")
elif user_choice == "rock" and comp_choice == "paper":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Lose")
elif user_choice == "rock" and comp_choice == "scissor":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Won")
elif user_choice == "paper" and comp_choice == "rock":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Won")
elif user_choice == "paper" and comp_choice == "scissor":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Lose")
elif user_choice == "scissor" and comp_choice == "rock":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Lose")
elif user_choice == "scissor" and comp_choice == "paper":
    print(f"User Choice: {user_choice}\nComputer Choice: {comp_choice}")
    print("You Won")
# print() is to add an empty line.
print()