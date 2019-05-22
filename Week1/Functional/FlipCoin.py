from random import *
try:
    trails = int(input("Enter Trials : "))
    head = 0
    tail = 0
    for i in range(trails):
        res = random()
        if res <= 0.5:
            head += 1
        else:
            tail += 1
    ph = round(((head / trails) * 100), 2)
    pt = round(((tail / trails) * 100), 2)
    print("Percentage Of Getting Head : ", ph)
    print("Percentage Of Getting Tail : ", pt)
except ValueError:
    print("\nInvalid Input Please Enter Integer..!")