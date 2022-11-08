# Rock Paper Scissors
# Zach Sally
# Topics - Lists

import random

user_wins = 0
cp_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    # Input not in list
    if user_input not in options:
        print("Invalid Option")
        continue

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors
    random_number = random.randint(0, 2)
    cp_pick = options[random_number]
    print("Computer picked " + cp_pick)

    # Win Conditions
    if user_input == options[0] and cp_pick == options[2]:
        print("You won!")
        user_wins += 1

    elif user_input == options[1] and cp_pick == options[0]:
        print("You won!")
        user_wins += 1

    elif user_input == options[2] and cp_pick == options[1]:
        print("You won!")
        user_wins += 1
    
    # Draw Condition
    elif user_input == cp_pick:
        print("It's a tie!")
    
    # Lose if didn't win or draw
    else:
        print("You lost!")
        cp_wins += 1

# End Game
print("Ended Game")
print("User Score = ", user_wins)
print("CP Score = ", cp_wins)
