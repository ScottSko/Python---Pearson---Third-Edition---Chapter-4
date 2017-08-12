total = 0

for b in range(5):
    if b == 0:
        bugs = int(input("How many bugs did you collect on the first day? "))
        total = total + bugs
    elif b == 1:
        bugs = int(input("How many bugs did you collect on the second day? "))
        total = total + bugs
    elif b == 2:
        bugs = int(input("How many bugs did you collect on the third day? "))
        total = total + bugs
    elif b == 3:
        bugs = int(input("How many bugs did you collect on the fourth day? "))
        total = total + bugs
    elif b == 4:
        bugs = int(input("How many bugs did you collect on the fifth day? "))
        total = total + bugs
print("You collected ", total, " bugs in 5 days.")
if total >= 50:
    print("Great job!")
elif total < 50:
    print("Not bad!")