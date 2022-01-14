#Simple Program Rock, Paper or Scissors
import random

choices = ["rock", "paper", "scissors"]

while True:
    machine=random.choice(choices)
    player=None
    while player not in choices:
     player=str(input("rock, paper or scissors: ")).lower()

    if player==machine:
        print("Computer: ", machine)
        print("Player: ", player)
        print("It's a tie")
    elif player=="rock" and machine=="scissors":
        print("Computer: ", machine)
        print("Player: ", player)
        print("Player wins")
    elif player == "scissors" and machine == "paper":
        print("Computer: ", machine)
        print("Player: ", player)
        print("Player wins")
    elif player=="paper" and machine=="rock":
        print("Computer: ", machine)
        print("Player: ", player)
        print("Computer wins")
    else:
        print("Computer: ", machine)
        print("Player: ", player)
        print("Computer wins")
    play_again=input("Play again? (y/n): ").lower

    if play_again != "y":
        break

print("Bye, thanks for playing!")



