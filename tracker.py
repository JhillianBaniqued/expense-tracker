# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Jhillian Denice A. Baniqued
# Description: A menu tracker that keeps runnng until user chooses to exit.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print()
    print("MAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses (coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total
        print(f"\tExpenses:\t{count}")
        print(f"\tSubtotal:\t${subtotal}")
        print(f"\tTax ({tax_percent}%):\t${tax}")
        print(f"\tGrand total:\t${total}")
        if over_budget:
            print(f"\tOver budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"\tCareful: only ${left} left.")
        else:
            print(f"\tWithin budget. ${left} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Jhillian Denice A. Baniqued | Installment 5")
print("=" * 40)