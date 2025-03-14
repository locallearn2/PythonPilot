"""
Task 5: Merging & Integration
📌 Goal: Combine all sections into a working program.

✅ What to do:
1. Ensure the user input from Task 1 flows into Task 2.
   - The name should be stored and used throughout the program.
2. Pass the user’s membership type and spending details to Task 2 and Task 3.
3. Ensure Task 2 correctly applies membership discounts.
4. Ensure Task 3 correctly applies high spender discounts.
5. Task 4 should compute the final amount and format the receipt.
6. Test the entire program for errors, ensuring all user inputs and outputs work smoothly.
7. As a team, review and refine the final program to ensure clarity and a smooth user experience.
"""

name = input("What is your name?")
if not name:
    print ("You didn't enter your name, please try again.")
    name = input("What is your name?")

else:
    print(f"Hello, {name}!")

membership_type = input("What is your membership type? (Regular, Premium, VIP)")
if not membership_type:
    print ("Invalid membership type. Please enter Regular, Premium, or VIP.")
    membership_type = input("What is your membership type? (Regular, Premium, VIP)")

else:
    print(f"Thank you! You are a {membership_type} member!")

amount = int(input("Enter the total amount spent:"))
if (amount < 0):
    print ("Amount must be a positive number. Please enter again.")
    amount = input("Enter the total amount spent:")

else:
    print(f"Thank you! You owe {amount}")

if membership_type == "VIP":
    discount = 0.3
    print ("VIP membership detected. Applying 30% discount.")
elif membership_type == "Premium":
    discount = 0.2
    print ("Premium membership detected. Applying 20% discount.")
else:
    discount = 0.1
    print ("Regular membership detected. Applying 10% discount.")

extra_discount = 0
if (amount > 500):
    extra_discount+= .1
    print("High spender detected! Additional 10% discount applied.")
    if (amount > 200):
      extra_discount+=.05
      print("Spending over $200! Additional 5% discount applied.")
else:
    print("No discount applied.")

total_discount = discount + extra_discount
print(f"Total discount applied: {total_discount}%")
final_total = amount - (amount * total_discount)
print(f"Final price after discount: ${final_total:.2f}")
print(f"""
--------------------------
--- Online Store Receipt ---
Name: {name}
Membership Type: {membership_type}
Total Spent: ${amount:.2f}
Membership Discount: {discount}%
Extra Discount: {extra_discount:.2f}%
--------------------------
Total Discount: {total_discount}%
Final Amount to Pay: ${final_total:.2f}
--------------------------
Thank you for shopping with us!""")