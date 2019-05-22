from Week1.Util import calc_change
try:
    rupees=int(input("Enter Amount To Return Change : "))
    calc_change(rupees)
except ValueError:
    print("\nInvalid Input Enter Numeric Value..!")