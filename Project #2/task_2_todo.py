"""
Task 2: Apply Discounts Based on Membership
📌 Goal: Determine the discount based on membership type.

✅ What to do:
🔹 If VIP, apply a 30% discount.
   - Example: Output something like "VIP membership detected. Applying 30% discount."
🔹 If Premium, apply a 20% discount.
   - Example: Output something like "Premium membership detected. Applying 20% discount."
🔹 If Regular, apply a 10% discount.
   - Example: Output something like "Regular membership detected. Applying 10% discount."
🔹 Store the discount percentage for later calculations.
"""
membership_type = input("What is your membership type? (Regular, Premium, VIP)")

if membership_type == "VIP":
    discount = 0.3
    print ("VIP membership detected. Applying 30% discount.")
elif membership_type == "Premium":
    discount = 0.2
    print ("Premium membership detected. Applying 20% discount.")
else:
    discount = 0.1
    print ("Regular membership detected. Applying 10% discount.")
    
    

