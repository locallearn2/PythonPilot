import random  # Importing random module for dice rolls

# 🎲 Dice-Based Racing Game - Code Framework

# Task 1: Game Setup
# TODO: Print a welcome message introducing the game.
# TODO: Ask Player 1 for their name and store it in a variable.
# TODO: Ask Player 2 for their name and store it in a variable.
# TODO: Initialize both players' scores to 0.
# TODO: Display the starting scores for both players.
# TODO: Set up a variable to track whose turn it is (Player 1 starts).

print ("🎲 Welcome to the Dice Racing Game!")
player_1 = input("Enter Player 1's name: ")
player_2 = input("Enter Player 2's name: ")
score_1 = 0
score_2 = 0
print (f"Scores: {player_1} - {score_1} | {player_2} - {score_2}")
turn = 1
while(True):
    if turn == 1:
       player, score = player_1, score_1 
    else:
        player, score = player_2, score_2
    prompt = input(f"{player}, press Enter to roll...")
    dice_roll = random.randint(1, 6)  # Generates a random number between 1 and 6
    print(f"🎲 {player} rolled a {dice_roll}!")
    score += dice_roll
    # special event
   
    if (dice_roll == 6):
        print("Extra roll awarded!")
        dice_roll = random.randint(1, 6)  # Generates a random number between 1 and 6
        print(f"🎲 {player} rolled a {dice_roll}!")
        score += dice_roll
    elif(dice_roll==1):
        if (score - 2) > 0:
            score -= 2
        else:
            score = 0
        print("Oops! You stumbled and lost 2 points.")
    if (score==15):
        score += 5
        print("Turbo boost activated! +5 points added!")

    print(f"New score: {score}")
    
    
    # Task 4: Checking for a Winner & Ending the Game
    if (score >20):
        print(f"{player} wins the race with 20 points!")
        break
        
    if turn == 1:
        score_1 = score
        turn = 2
    else:
        score_2 = score
        turn = 1
    
    print(f"Scores: {player_1} - {score_1} | {player_2} - {score_2}")
    
print("Game Over. Thanks for playing!")

# Task 2: Player Turn & Dice Roll
# TODO: Prompt the current player to press Enter to roll the dice.
# TODO: Display the result of the dice roll.
# TODO: Add the dice roll result to the current player's score.


# Task 3: Special Race Events
# TODO: If the player rolls a 6, print a message and allow an extra roll.
# TODO: If the player rolls a 1, print a message and subtract 2 points (ensure score doesn't go below 0).
# TODO: If the player's score reaches exactly 15, print a message and add a 5-point turbo boost.


# Task 5: Turn Management & Game Continuation
# TODO: Switch turn to the next player after each roll.
# TODO: Ensure turns alternate correctly between players.
# TODO: At the end of the game, display a final message and ask if they want to play again.
# TODO: If the players choose to restart, reset all scores and begin a new game loop.
