"""
Task 5: Merging & Integration
📌 Goal: Combine all sections into a working program.

✅ What to do:
1. Ensure the user input from Task 1 flows into Task 2.
   - The name should be stored and used throughout the program.

2. Pass the user’s selected menu choices from Task 2 to Task 3.
   - The drink, entrée, and dessert choices should be consistent.

3. Ensure Task 3 correctly calculates and formats the receipt.

4. The formatted receipt from Task 3 should be displayed correctly in Task 4.

5. Test the entire program for errors, ensuring all user inputs and outputs work smoothly.

6. As a team, review and refine the final program to ensure clarity and a smooth user experience.

"""
print("Welcome to Python Cafe")
name_var = input("What is your name?")
print(f"Hi {name_var}, here is our menu")
menu = f"""
-------- Python Cafe Menu --------
Drinks: Coffee ($5), Tea ($5), Milk ($5)
Entrees: Pasta ($15), Bread ($15), Fish ($15)
Dessert: Ice Cream!!!! ($10), Brownie ($10), Donut ($10), Cake ($10)"""
print(menu)

drink_var = input("Hi {name_var}, what would you like to drink?")
entree_var = input("And what would you like for your entrée?")
dessert_var = input("Finally, what would you like for dessert?")

drink_price = 5
entree_price = 15
dessert_price = 10
subtotal = drink_price + entree_price + dessert_price
tax = subtotal * .1
tip = subtotal * .15
total =subtotal + tax + tip
receipt = f"""
   --------------------------
   --- Python Café Receipt ---  
   Name: {name_var}  
   Drink: {drink_var} - ${drink_price}  
   Entrée: {entree_var} - ${entree_price}  
   Dessert: {dessert_var} - ${dessert_price}  
   --------------------------  
   Subtotal: ${subtotal:.2f}  
   Tax (10%): ${tax:.2f}  
   Tip (15%): ${tip:.2f}  
   Total: ${total:.2f}  
   --------------------------  
   Thank you for dining with us!  
"""
print(f'So, {name_var}, you ordered {drink_var}, {entree_var}, and {dessert_var}.')
print(receipt)
print(f"Thank you for dining at Python Café, {name_var}! Enjoy your meal!")