budget = int(input("How much have you budgeted for the month? "))
tallying = "y"
total = 0.0

while tallying != "n" or "N" or "No" or "no" or "NO":
    expense = float(input("What was your expense? "))
    total += expense
    tallying = input("Would you like to enter another expense? (y/n)")

if total > budget:
    print("You are", total - budget, "over budget")
elif total < budget:
    print("You are", budget - total, "under budget")