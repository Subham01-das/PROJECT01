import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num, highest_num)
guesses=0
is_running=True

print("python guess the number game")
print(f"Guess a number between {lowest_num} and {highest_num}")
while is_running:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
        print(f"Your guess must be between {lowest_num} and {highest_num}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} in {guesses} tries.")
        is_running = False
 