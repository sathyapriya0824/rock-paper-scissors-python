import random

print("---- Rock Paper Scissors Game ----")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user = input("\nEnter rock / paper / scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Computer choice:", computer)

    if user == computer:
        print("It's a Draw!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You Win this round!")
        user_score += 1

    else:
        print("Computer Wins this round!")
        computer_score += 1

    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)

    play = input("\nPlay again? (yes/no): ").lower()

    if play != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Game Over!")
        break
