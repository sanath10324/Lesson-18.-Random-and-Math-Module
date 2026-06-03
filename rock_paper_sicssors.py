import random 

while True:
    user_actions = input("Enter a choice, (Rock, Paper, or Sicssors):")
    possible_actions = ["Rock","Paper","Sicssors"]
    computer_actions = random.choice(possible_actions)
    print("\n You chose {user_actions}, the computer chose {computer_actions}. \n")

    if user_actions == computer_actions:
        print("\n You and the computer chose the same thing, its a tie!!")
    elif user_actions == "Rock":
        if computer_actions == "Sicssors":
            print("Rock smashes Sicssors, you win!!")
        else:
            print("Paper covers Rock, you lose")
    elif user_actions == "Paper":
        if computer_actions == "Rock":
            print("Paper covers Rock, you win!!")
        else:
            print("Sicssors cut through paper, you lose")
    elif user_actions == "Sicssors":
        if computer_actions == "Paper":
            print("Sicssors cut through paper, you win!!")
        else: 
            print("Rock smashes sicssors, you lose")

    play_again = input("do you wanna play again? (y/n)")
    if play_again == "y":
        break