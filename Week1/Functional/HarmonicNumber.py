from Week1.Util import print_series
try:
    x = int(input("Enter Nth Harmonic Term : "))
    while x <= 0:
        x = int(input("Enter Nth Harmonic Term > 0 : "))
    print_series(x)
except:
    print("Invalid Input..!")