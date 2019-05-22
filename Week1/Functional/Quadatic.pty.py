from Week1.Util import find_roots
try:
    a = float(input("Enter Value Of a : "))  # Get Value Of a
    b = float(input("Enter Value Of b : "))  # Get Value Of b
    c = float(input("Enter Value Of c : "))  # Get Value Of c
    find_roots(a, b, c)                      # Call Function To Calculate Roots
except ValueError:
    print("\nEnter Valid Input..")