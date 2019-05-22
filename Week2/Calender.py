from util.dsutil import Calender
try:
    year = int(input("Enter Year : "))                  # Take Year Input
    while len(str(year)) <= 3:                          # Validate Year Length
        year = int(input("Enter Year > 4 Digit: "))

    month = int(input("Enter Month : "))                # Take Month Input
    while month > 12 or month <= 00:                    # Validate Month Value Less Than 12 and Greater Than 0
        month = int(input("Enter Month < 12 And > 0: "))

    cal = Calender()                                     # Create Calender Class Object
    cal.Show_Cal(year, month)                            # Call Show_Cal Function
except ValueError:
    print("\nEnter Number Value")