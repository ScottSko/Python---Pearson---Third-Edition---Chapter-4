speed = int(input("What is the speed of the vehicle in MPH? "))
hours = int(input("How many hours has it traveled? "))

print("Hour", "\t", "Distance Traveled")
print("_______________________________")

for x in range(hours):
    distance_traveled = ((x + 1) * (speed))
    print(x + 1, "\t \t \t \t", distance_traveled)
