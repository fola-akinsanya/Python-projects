from random import randint

#play options list
play = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = play[randint(0,2)]

#Computer plays - set player to False
player= False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?").capitalize()
    if player == computer:
        print("Tie!")
        print("Computer also played",computer)
    elif player == "Rock":
        if computer == "Paper":
            print("Computer played",computer)
            print("You lose!", computer, "covers", player)
        else:
            print("Computer played",computer)
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer played",computer)
            print("You lose!", computer, "cut", player)
        else:
            print("Computer played",computer)
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer played",computer)
            print("You lose!", computer, "smashes", player)
        else:
            print("Computer played",computer)
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Please check your spelling!")
    #reset player to False so the loop continues
    player = False
    computer = play[randint(0,2)]
