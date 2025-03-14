"""
Task 1: User Input & Menu Display
📌 Goal: Create a simple café menu and greet the customer.

✅ What to do:
1. Display a welcome message.
   - Example: Output something like "Welcome to Python Café!"

2. Ask the user for their name.
   - Example: Output something like "What is your name?"

3. Greet the user with their name.
   - Example: Output something like "Hi <name_var>, here is our menu!"

4. Display the menu, listing drinks, entrées, and desserts with their prices.
   - Example: "Drinks: Coffee ($5), Tea ($5)..."

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
