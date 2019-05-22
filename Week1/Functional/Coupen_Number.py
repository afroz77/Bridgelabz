import random
try:
    cp = int(input("How Many Coupen You Want To Generate : "))
    cplen = int(input("Enter Coupen Length : "))
    print("Generated Coupen Numbers :")
    count = 1
    cpnum = ''
    while count <= cp:
        temp = cpnum
        cpnum = ''
        for i in range(cplen):
            cpnum += str(random.randint(0, 9))
        if cpnum != temp:
            print(count, ":", cpnum)
            count += 1
except ValueError:
    print("\nInvalid Input Please Enter Numbers Only..!")
