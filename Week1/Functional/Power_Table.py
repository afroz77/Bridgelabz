try:
    num = int(input("Enter Nth Value : "))       # Get Value From User
    while num > 31:                              # Check Is Greater Than 31
        num = int(input("Enter Nth Value < 31: "))
    for n in range(1, num + 1):                  # Loop To Calculate Power
        print("2^", n, "=", 2 ** n)
except ValueError:
    print("Invalid Input..")