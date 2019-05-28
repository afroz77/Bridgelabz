from Week1.Util import CalcPayment

"""
    MonthPayment Method Ask User To 3 Input As
    1. Principle Amount as P
    2. Years To Pay as Y
    3. Rate Of Interest As R
    
    Pass All Three Input To The Util Function CalcPayment()
"""


def MonthPayment():
    try:
        P = float(input("Enter Principle Amount : "))       # Ask For P Input
        Y = float(input("Enter Years To Pay Off  : "))      # Ask For Y Input
        R = float(input("Enter Rate Of Interest : "))       # Ask For R Input
        CalcPayment(P, Y, R)                                # Call Util Function And Pass The Inputs
    except ValueError:
        print("Invalid Input ")                             # Validation Error
        MonthPayment()                                      # Call Self


"""
    Main Method
"""
if __name__ == '__main__':
    MonthPayment()    # Function Call
