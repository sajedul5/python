import random

while True:
    choices = ["rock","paper","scissors"]

    computur = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computur:
        print("Computer: ", computur)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computur == "paper":
            print("Computer: ", computur)
            print("player: ", player)
            print("You lose!")
        if computur == "scissors":
            print("Computer: ", computur)
            print("player: ", player)
            print("You win!")
    elif player == "paper":
        if computur == "scissors":
            print("Computer: ", computur)
            print("player: ", player)
            print("You lose!")
        if computur == "rock":
            print("Computer: ", computur)
            print("player: ", player)
            print("You win!")
    elif player == "scissors":
        if computur == "rock":
            print("Computer: ", computur)
            print("player: ", player)
            print("You lose!")
        if computur == "paper":
            print("Computer: ", computur)
            print("player: ", player)
            print("You win!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")