days = int(input("How many days? "))
total = 0
pennies = 1
total_pennies = 0

print("Day", "\t", "Salary")
print("____________________")

for x in range(days):

    total_pennies = pennies
    pennies = total_pennies * 2

    salary = ((total_pennies) * .01)
    total += salary
    print(x + 1, "\t", salary)

print("You earned a total of", total, "dollars.")


