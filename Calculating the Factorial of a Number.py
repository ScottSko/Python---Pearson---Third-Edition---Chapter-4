factorial_input = int(input("Please enter a nonnegative integer: "))
#factorial_hold = factorial_input
total = 1

while factorial_input <= 0:
    print("Error")
    factorial_input = int(input("Please enter a nonnegative integer: "))
    factorial_hold = factorial_input

for x in range(factorial_input):
        factorial = x + 1 # = factorial_input
        #factorial_input -= 1
        total *= factorial

print("The factorial of ", factorial_input, "is", total)