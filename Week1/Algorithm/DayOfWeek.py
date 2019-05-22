from Week1.Util import DayOfWeek

try:
    day = int(input("Enter Day : "))              # Get Input Day Value
    while day > 31:                               # Validate Day Value < 31
        day=int(input("Enter Valid Day < 31 :"))
    month = int(input("Enter Month : "))          # Get Input Month Value
    while month > 12:                             # Validate Month Value < 12
        month=int(input("Enter Valid Month < 12 :"))
    year = int(input("Enter Year : "))            # Get Input Year Value
    while len(str(year))<4:                       # validate Year Value Length >= 4
        year = int(input("Enter Valid Year : "))
    DayOfWeek(day, month, year)                   # Call Util Function DayOfWeek
except:
    print("\nInvalid Input Enter Only Numbers ")
