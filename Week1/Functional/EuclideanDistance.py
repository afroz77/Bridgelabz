from Week1.Util import calculateDistance
import sys as s

try:
    # x=float(s.argv[1])
    # y=float(s.argv[2])
    x=float(input("Enter Value Of X : "))
    y=float(input("Enter Value Of Y : "))
    print("\nThe Distance Is :",round(calculateDistance(x, y),2))
except:
    print("\nInvalid Input...!")