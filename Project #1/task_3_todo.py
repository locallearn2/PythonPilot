"""
Task 3: Price Calculation & Receipt Formatting
📌 Goal: Compute the total cost and format the receipt.

✅ What to do:
1. Assign fixed prices:
   - Drinks: $5
   - Entrées: $15
   - Desserts: $10

2. Calculate the subtotal before tax.

3. Compute a 10% tax on the subtotal.

4. Compute a 15% tip on the subtotal.

5. Compute the final total (subtotal + tax + tip).

6. Format the receipt using string formatting (f-strings, .format(), etc.), but DO NOT print it yet—store it in a variable for later use.

   Example format:
   --------------------------
   --- Python Café Receipt ---  
   Name: <name_var>  
   Drink: <drink_var> - $5  
   Entrée: <entrée_var> - $15  
   Dessert: <dessert_var> - $10  
   --------------------------  
   Subtotal: $XX.XX  
   Tax (10%): $XX.XX  
   Tip (15%): $XX.XX  
   Total: $XX.XX  
   --------------------------  
   Thank you for dining with us!  

"""
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