player1 = input("player 1, enter your choice (rock,paper,or scissors):").lower()
player2 = input("player 2, enter your choice (rock,paper,or scissors):").lower()
if player 1 == player 2:
   print("it's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    print("player 1 wins!")
else:
   print("player 2 wins!")
new_game = input("Do you want to start a new game ? (yes/no):")
if new_game.lower() == "yes":
    print("starting a new game...")
else :
      print("thanks for playing !")
