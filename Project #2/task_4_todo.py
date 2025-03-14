"""
Task 4: Final Price Calculation & Summary
📌 Goal: Calculate the final total and print a receipt.

✅ What to do:
🔹 Calculate total discount (membership + extra discount).
   - Example: Output something like "Total discount applied: X%."
🔹 Compute the final price after applying the discount.
   - Example: Output something like "Final price after discount: $X.XX"
🔹 Print a receipt summarizing:
   - User’s name
   - Membership type
   - Total amount spent
   - Discounts applied
   - Final amount to pay
🔹 Print a final thank-you message.
   - Example: Output something like "Thank you for shopping with us!"

📄 Example Output Receipt:
--------------------------
--- Online Store Receipt ---
Name: John
Membership Type: Premium
Total Spent: $250
Membership Discount: 20%
Extra Discount: 5%
--------------------------
Total Discount: 25%
Final Amount to Pay: $187.50
--------------------------
Thank you for shopping with us!
"""

total_discount = member_discount + extra_discount
print(f"Total discount applied: {total_discount}%")
final_total = total * total_discount
print(f"Final price after discount: ${total_price}")
print("""
--------------------------
--- Online Store Receipt ---
Name: {name}
Membership Type: {membership}
Total Spent: ${total:.2f}
Membership Discount: {member_discount}%
Extra Discount: {extra_discount}%
--------------------------
Total Discount: {total_discount}%
Final Amount to Pay: ${final_total:.2f}
--------------------------
Thank you for shopping with us!""")


