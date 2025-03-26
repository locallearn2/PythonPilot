🎲 Dice-Based Racing Game
⏳ Duration: ~2 hours
👥 Group Size: 4
🛠 Concepts Used: 
✅ Loops (while, for) 
✅ Conditional statements (if, elif, else) 

🚗 Overview
Welcome to the Dice-Based Racing Game! In this exciting turn-based game, players will race to the finish line by rolling a virtual die. Each player takes turns rolling, advancing their score based on the result. But beware—random events like speed boosts and penalties can change the outcome of the race in unexpected ways!
The game continues until one player reaches 20 or more points, at which point they are declared the winner. Players must strategize, roll wisely, and hope luck is on their side as they race toward victory!
This project is designed to strengthen your understanding of loops, conditional statements, and user input handling in Python, making it a fun and educational challenge for your group.

🔀 Task Breakdown
🔹 Task 1: Game Setup & Player Turn Order
📌 Goal: Display game rules and set up turn order.
✅ What to do:
Print a welcome message explaining the game.
Example: 🎲 Welcome to the Dice Racing Game!
Ask for each player’s name (store in separate variables).
Example: Player 1: John
Example: Player 2: Sarah
Display the starting scores (all 0).
Example: Scores: John - 0 | Sarah - 0
Set up a turn-based system using a while loop:
Use a variable to track whose turn it is.
Continue looping until a winner is determined.
Prompt the correct player for input each turn.
Ensure turns alternate between players correctly.

🔹 Task 2: Rolling the Die & Moving Forward
📌 Goal: Let each player roll a "die" (random number 1-6) and update their score.
✅ What to do:
On each turn, prompt the current player to "press Enter to roll the die".
Example: John, press Enter to roll...
Generate a random number (1-6) and display the result.
Example: 🎲 John rolled a 5!
Add the result to the player’s total score.
Example: New score: 5
Display the updated scores after each roll.
Example: Scores: John - 5 | Sarah - 0
Ensure that after each turn, control is passed to the next player.

🔹 Task 3: Adding Race Events (Speed Boosts & Penalties!)
📌 Goal: Introduce random events based on dice rolls.
✅ What to do:
If the player rolls a 6, they get an extra roll:
Allow them to roll again immediately.
Ensure their extra roll is properly counted toward their total score.
Example: 🎲 Sarah rolled a 6! Extra roll awarded!
If they roll a 1, they "stumble" and lose 2 points (but no negatives!):
Subtract 2 from their score only if it doesn’t drop below zero.
Example: Oops! You rolled a 1 and lost 2 points.
If they land on exactly 15 points, they get a "turbo boost" (+5 points):
Check if their score is exactly 15 before applying the bonus.
Example: Turbo boost activated! +5 points added!
Display messages based on events.

🔹 Task 4: Determining the Winner & Ending the Game
📌 Goal: Check if someone reaches 20+ points and declare the winner.
✅ What to do:
After every roll, check if a player's score is 20 or higher.
If a player has reached or exceeded 20, print a victory message.
Example: 🎉 Sarah wins the race with 21 points!
If a player wins, exit the game loop immediately.
Ask if players want to restart the game (loop again) or exit:
Prompt the user for a yes/no response.
If they choose to restart, reset all scores and start over.
Example: Game Over. Play again? (yes/no)

🤝 Collaboration & Integration Guide
✔ Use separate variables for each player's score (no lists!).
✔ Use a loop to keep the game running until someone wins.
✔ Ensure turns alternate correctly between players.
✔ Use clear print statements to show progress and make it fun.
✔ Test each section independently before merging.

🚀 Happy coding and good luck with the race!


