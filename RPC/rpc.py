

import random

options = ["rock", "paper", "scissors"]



running =True
while(running):
    player = None
    computer = random.choice(options) 
    player = input("enter the choice (rock, paper,scissors):") 
    while player not in options:
        print("invalid option:")
        print("pick again")
        player = input("enter the choice (rock, paper,scissors):  ") 




    print("player:", player)

    print("computer:", computer)

    if player==computer: print("its a tie")
    elif player=="rock" and computer == "scissors":print("you win!")
    elif player == "paper" and computer == "rock": print("you win!")
    elif player == "scissors" and computer == "paper": print("you win!")
    else:print("you loose!")
    x=input("type '1' to play again, type '0' to quit:  ")
    if not x=="1":running=False
print("Thanks for playing")


        
