import random
item_list = ["rock", "paper", "scissors"]
user_choice=input("Enter your move = rock, paper, or scissors: ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
