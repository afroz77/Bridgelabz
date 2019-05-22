import sys
from Week1.Util import CalcPayment

try:
    P = float(input("Enter Principle Ampunt : "))
    Y = float(input("Enter Years To Pay Off  : "))
    R = float(input("Enter Rate Of Interest : "))
    CalcPayment(P, Y, R)
except:
    print("Invalid Input ")

