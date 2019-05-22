from util.dsutil import Calender
try:
    year = int(input("Enter Year : "))                  # Take Input As Year
    while len(str(year)) <= 3:                          # check length of year
        year = int(input("Enter Year > 4 Digit: "))     # again  popup for input

    month = int(input("Enter Month : "))                # Take Input As Month
    while month > 12 or month <= 00:                    # check month less than 12 and greater than 0
        month = int(input("Enter Month < 12 And > 0: "))

    cal = Calender()                                    # create Calender Class object
    cal.Show_Cal_Queue(year, month)                     # Call Show_Cal_Queue Function
except ValueError:
    print("\nEnter Number Value")                       # Print Value Error