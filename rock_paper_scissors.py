import random

user_win = 0
computer_win = 0
while True:
    computer_choice = random.randint(1, 3)
    user_input = input("Choose [r]ock , [p]aper or [s]cissors ( [E]nd fo exit) :\n")
    if user_input.lower() == "e":
        break

    computer_choice_string = ""
    if computer_choice == 1:
        computer_choice_string = "Rock"
    elif computer_choice == 2:
        computer_choice_string = "Paper"
    else:
        computer_choice_string = "Scissors"

    if user_input.lower() == "r":
        if computer_choice == 1:
            print("Draw")

        elif computer_choice == 2:
            print("You lose, try again:")
            computer_win += 1
        else:
            print("You WIN, lets play again: ")
            user_win += 1
    elif user_input.lower() == "p":
        if computer_choice == 1:
            print("You WIN, lets play again: ")
            user_win += 1

        elif computer_choice == 2:
            print("Draw")
        else:
            print("You lose, try again:")
            computer_win += 1
    elif user_input.lower() == "s":
        if computer_choice == 1:
            print("You lose, try again:")
            computer_win += 1

        elif computer_choice == 2:
            print("You WIN, lets play again: ")
            user_win += 1
        else:
            print("Draw")
    else:
        print("INVALID INPUT")
if user_win > computer_win:
    print(f"User won the game with score {user_win} : {computer_win}")
elif user_win < computer_win:
    print(f"Computer won the game with score {computer_win} : {user_win}")
else:
    print("The game was draw ! ")
