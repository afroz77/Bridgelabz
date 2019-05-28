from Week1.Util import Decimal_To_Binary

"""
    Function To Convert The Decimal Numbner To Binary
    Which Ask User To Enter A Number And Calculate The Binary Number Of Given Number

"""


def DecimalToBinary():
    try:
        ch = 'Y'                # Declare Ch For Asking The Another Number To Convert
        while ch.upper() == "Y":    # While loop Till The User Enters y
            num = int(input("Enter a Number : "))       # Ask User To Enter A Number
            if not str(num).isnumeric():                # Validate User Input If Not Numeric
                raise ValueError                        # Raise Value Error
                return                                  # Return From Method Go To except
            res = Decimal_To_Binary(num)                # Pass The Number To Function And Accept One String Number
            print("Binary Conversion Of", num, "=", res)        # Print The Number
            ch = input("\nDo You Want To Convert Another y/n : ")   # Ask User To Convert Another If y Then Yes Else
        print("Bye..")                                              # Terminate The Loop
    except ValueError:                              # Handle Error
        print("Invalid Input Enter Number Only..")  # Print Error Message
        DecimalToBinary()                           # Call Self


"""
    Main Method And Call The Above Function
"""
if __name__ == '__main__':
    DecimalToBinary()       # Function Call
