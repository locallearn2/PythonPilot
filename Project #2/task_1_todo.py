"""
Task 1: User Input & Order Details
📌 Goal: Collect the necessary details from the user.

✅ What to do:
🔹 Ask for the user’s name.
   - Example: Output something like "What is your name?"
🔹 If they don’t enter anything, print an error message and ask again.
   - Example: Output something like "You didn't enter your name, please try again."
🔹 Ask for their membership type (Regular, Premium, VIP).
   - Example: Output something like "What is your membership type?"
🔹 If the input is invalid, display an error message and ask again.
   - Example: Output something like "Invalid membership type. Please enter Regular, Premium, or VIP."
🔹 Ask for the total amount spent at checkout.
   - Example: Output something like "Enter the total amount spent:"
🔹 If the input is not a positive number, display an error message and ask again.
   - Example: Output something like "Amount must be a positive number. Please enter again."
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