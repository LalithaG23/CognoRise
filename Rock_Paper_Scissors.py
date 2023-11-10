import random

options = ("ROCK", "PAPER", "SCISSORS")

print("Rock, Paper, Scissors Game")
score=0

playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(Rock, Paper, Scissors):").upper()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("IT'S A TIE!")
        elif player == "ROCK" and computer == "SCISSORS":
            print("YOU WIN !")
            score +=1
        elif player == "PAPER" and computer == "ROCK":
            print("YOU WIN !")
            score +=1
        elif player == "SCISSORS" and computer == "PAPER":
            print("YOU WIN !")
            score +=1
        else:
            print("OOPS! TRY AGAIN")

        play_again = input("Play again? (y/n):").lower()
        if not play_again == "y":
            playing = False
        


print(f"Your Score:{score}")
print("Thanks for Playing!")

        





