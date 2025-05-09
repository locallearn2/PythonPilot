🛒 Project: Online Store Discount Calculator 
⏳ Duration: ~1 hours
👥 Group Size: 4
🛠️ Concepts Used: 
✅ if, if-else, elif statements
✅ Boolean logic & logical operators (and, or, not)
✅ Nested conditionals
✅ Ternary operators

📜 Project Overview
Welcome to the Online Store Discount Calculator project! In this assignment, you will create a discount calculator for an online store using Python. You will work in a group of four, with each person responsible for a specific task. By the end, your program will allow a user to input their details, determine applicable discounts based on membership and total spending, compute the final price, and generate a formatted receipt.

🔀 Project Breakdown
Each team member will complete one task. The tasks are designed to connect smoothly, so work together to ensure consistency.
Task 1: User Input & Order Details
📌 Goal: Collect the necessary details from the user.
✅ What to do: 
🔹 Ask for the user’s name.
Format Example: Output something like "What is your name?"
🔹 If they don’t enter anything, print an error message and ask again.
Format Example: Output something like "You didn't enter your name, please try again."
🔹 Ask for their membership type (Regular, Premium, VIP).
Format Example: Output something like "What is your membership type?"
🔹 If the input is invalid, display an error message and ask again.
Format Example: Output something like "Invalid membership type. Please enter Regular, Premium, or VIP."
🔹 Ask for the total amount spent at checkout.
Format Example: Output something like "Enter the total amount spent:"
🔹 If the input is not a positive number, display an error message and ask again.
Format Example: Output something like "Amount must be a positive number. Please enter again."

Task 2: Apply Discounts Based on Membership
📌 Goal: Determine the discount based on membership type.
✅ What to do: 
🔹 If VIP, apply a 30% discount.
Format Example: Output something like "VIP membership detected. Applying 30% discount."
🔹 If Premium, apply a 20% discount.
Format Example: Output something like "Premium membership detected. Applying 20% discount."
🔹 If Regular, apply a 10% discount.
Format Example: Output something like "Regular membership detected. Applying 10% discount."
🔹 Store the discount percentage for later calculations.

Task 3: Extra Discounts for High Spenders
📌 Goal: Add extra discounts if the purchase is above certain amounts.
✅ What to do: 
🔹 If the total amount spent is $500+, apply an additional 10% discount.
Format Example: Output something like "High spender detected! Additional 10% discount applied."
🔹 If the total amount spent is $200+, apply an additional 5% discount.
Format Example: Output something like "Spending over $200! Additional 5% discount applied."
🔹 Use logical operators (and, or) to check conditions.
🔹 Store the extra discount percentage for later calculations.

Task 4: Final Price Calculation & Summary
📌 Goal: Calculate the final total and print a receipt.
✅ What to do: 
🔹 Calculate total discount (membership + extra discount).
Format Example: Output something like "Total discount applied: X%."
🔹 Compute the final price after applying the discount.
Format Example: Output something like "Final price after discount: $X.XX"
🔹 Print a receipt summarizing: User’s name, Membership type, Total amount spent, Discounts applied, Final amount to pay
🔹 Print a final thank-you message.
Format Example: Output something like "Thank you for shopping with us!"
Example Output Receipt:
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

🤝 Collaboration & Integration Guide
✔ Ensure consistent variable names (e.g., user_name, membership_type, total_spent, etc.).
✔ Each task depends on the previous one—test each section individually before merging.
✔ Use formatted strings (f-strings) for clear output.
✔ The person working on Task 4 should confirm that the receipt formatting is correct.
Happy coding! 🚀


