
try:
    year = int(input("Enter Year : "))   # Get Input Year From User
    while len(str(year)) < 4:            # Check Length Greater Than 4
        year = int(input("Enter Proper Value : "))
    print("\nLeap Year ") if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else print("\nNot a Leap Year ")
except:
    print("\nInvalid Input..!")