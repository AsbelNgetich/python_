import random


player_total=0
computer_total=0

while True:
    player_input = int(input("Please pick a number. Pick #1 for Rock  #2 for paper and #3. for scissors): "))


    player_pick=""
    if player_input==1:
        player_pick="Rock"
    elif player_input==2:
        player_pick="Paper"
    elif player_input==3:
        player_pick="scissors"

    computer_input = random.randint(1,3)
    computer_pick=""

    if computer_input==1:
        computer_pick="Rock"
    elif computer_input==2:
        computer_pick="Paper"
    elif computer_input==3:
        computer_pick="scissors"

    print(f"\nYou picked {player_pick}, and the computer picked {computer_pick}.\n")

    if player_input == computer_input:
        print(f"Both players selected {player_pick}. It's a tie")
    elif player_input == 1:
        if computer_input == 3:
            player_total +=1
            print("Rock beats Scissors. You win.")
        else:
            computer_total +=1
            print("Paper covers rock. You lose.")
    elif player_input == 2:
        if computer_input == 1:
            player_total +=1
            print("Paper covers rock. You win.")
        else:
            computer_total +=1
            print("Scissors cuts paper! You lose.")
    elif player_input == 3:
        if computer_input == 2:
            player_total +=1
            print("Scissors cuts paper. You win.")
        else:
            computer_total +=1
            print("Rock beats scissors. You lose.")
    
    if player_total==3:
        print("You have 3 points, you won the game!")
        break
    elif computer_total==3:
        print("The computer has 3 points, you lost to a Computer :(")
        break