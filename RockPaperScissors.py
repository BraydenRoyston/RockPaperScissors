print("Welcome to rock paper scissors!")
print("Decide who will be player 1 and player two, then enter either 'rock', 'paper' or 'scissors' to choose your move!")
print("Remember to look away while your oppenent is typing for a fair game.")


response = "yes"
while response == "yes":
    player1 = input("Player 1, enter your move:")
    player2 = input("Player 2, enter your move:")
    if player1 == "rock" or "paper" or "scissors" and player2 == "rock" or "paper" or "scissors":
        if player1 == "rock":
            if player2 == "rock":
                print("Tie!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "paper":
                print("Player 2 wins!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "scissors":
                print("Player 1 wins!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
        elif player1 == "paper":
            if player2 == "rock":
                print("Player 1 wins!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "paper":
                print("Tie!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "scissors":
                print("Player 2 wins!") 
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()   
        elif player1 == "scissors":
            if player2 == "rock":
                print("Player 2 wins!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "paper":
                print("Player 1 wins!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
            if player2 == "scissors":
                print("Tie!")
                print("Do you want to play again? Enter 'yes' or 'no'.")
                response = input()
if response == "no":
    print("Thanks for playing!")