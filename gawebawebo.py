"""
This is a rock paper scissors game

==================================
chapter 1 ...   RULE!!!
==================================

We play 10 games with Computer!!!
end of the game We print your score
and computer's score !!!

Have a nice game ~~~~
"""





import random

player_score = 0
computer_score = 0
play = True
n = 0
while play :
    if n == 10:
        break
    #player_choice
    player = input("Enter your choice (rock/paper/scissors): ")
    player = player.lower()
    while (player != "rock" and player != "paper" and player != "scissors"):
        player = input("Enter your choice (rock/paper/scissors): ")
        player = player.lower()

    #computer_random
    computer = random.randint(1,3)
    if (computer == 1):
        computer = "rock"
        print("comper's choise : rock" )
    elif (computer == 2):
        computer = "paper"
        print("comper's choise : paper" )
    elif (computer == 3):
        computer = "scissors"
        print("comper's choise : scissors" )
    else:
        print ("Error. Enter your choice from rock, paper, scissors.")

    #result

    if (player == "rock"):
        if (computer == "paper"):
            computer_score += 1
        if (computer == "scissors"):
            player_score += 1
    elif (player == "paper"):
        if (computer == "rock"):
             player_score += 1
        if (computer == "scissors"):
            computer_score += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            computer_score += 1
        if (computer == "paper"):
            player_score += 1
    n += 1
print(player_score,":",computer_score)
if(player_score>computer_score):
    print("player win!")
if(player_score==computer_score):
    print("draw...")
if(player_score<computer_score):
    print("coputer win!")
