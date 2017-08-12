num_steps = 7

for c in range(7, 0, -1):
    for r in range(c):
        print("*", end='')
    print("")



second_picture = 6

for c in range(second_picture):
    print("#", end='')
    for r in range(c):
        print(" ", end='')
    print("#")