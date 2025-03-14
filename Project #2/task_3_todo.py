"""
Task 3: Extra Discounts for High Spenders
📌 Goal: Add extra discounts if the purchase is above certain amounts.

✅ What to do:
🔹 If the total amount spent is $500+, apply an additional 10% discount.
   - Example: Output something like "High spender detected! Additional 10% discount applied."
🔹 If the total amount spent is $200+, apply an additional 5% discount.
   - Example: Output something like "Spending over $200! Additional 5% discount applied."
🔹 Use logical operators (and, or) to check conditions.
🔹 Store the extra discount percentage for later calculations.
"""

extra_discount = 0
if (total > 500):
    extra_discount+= .1
    print("High spender detected! Additional 10% discount applied.")
elif (total > 200):
    extra_discount+=.05
    print("Spending over $200! Additional 5% discount applied.")
else:
    print("No discount applied.")