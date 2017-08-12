tuition = 8000

for x in range(5):
    tuition += (tuition * .03)
    print("The tuition for year", x + 1, "is", format(tuition, ",.2f"))