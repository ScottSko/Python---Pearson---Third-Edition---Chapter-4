starting_organisms = int(input("Starting number of organisms: "))
daily_increase = float(input("Average daily increase: "))
days_to_multiply = int(input("Number of days to multiply: "))

population = starting_organisms

print("Day Approximate", "\t", "Population")

for x in range(days_to_multiply):
    starting_organisms = population
    population = starting_organisms + (starting_organisms * (daily_increase * .01))

    print(x + 1, "\t \t \t \t \t", starting_organisms)