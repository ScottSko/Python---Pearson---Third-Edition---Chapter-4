number = 0
total = 0

while number >= 0:
    number = int(input("Please enter a positive number (or a negative number to stop): " ))
    total += number

print("The total is ", total - number)