import random

# 1. Create a list of options
options = ["rock", "paper", "scissors"]

# 2. The computer picks a random option from the list
computer_choice = random.choice(options)

# 3. Get the user's choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

print(f"Computer chose: {computer_choice}")

# 4. Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock smashes Scissors.")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper covers Rock.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors cut Paper.")
else:
    print("You lose!")