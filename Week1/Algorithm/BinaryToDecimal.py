from Week1.Util import Decimal_To_Binary

"""
    Class DecimalToBinary Have One Function ConvertToBinary

"""


class DecimalToBinary:

    """
        ConvertToBinary Function AskUser To Enter A Number
        And Validate The Input After That Convert The Input And Print The Result

    """
    def ConvertToBinary(self):
        try:
            num = input("Enter a Number : ")   # Ask User For Enter A Number To Convert
            if not num.isnumeric():            # Validate The Input If Not Numeric
                raise ValueError               # Raise Value Error
        except ValueError:                     # Handle The Error
            print("Invalid Input ")            # Print Error Message
            self.ConvertToBinary()             # Call Self For Input
        else:                                  # Else
            temp = num                         # Store Number In Temp Variable
            res = Decimal_To_Binary(int(num))       # Calculate Binary Conversion Of The Number
            print("Binary Conversion Of", temp, "=", res)   # Print Binary Number Of The Number
            res = res[::-1]                                 # Reverse The String
            while len(res) <= 7:               # Loop Through The Length And Append 0 Till The Length Is 8
                res += '0'
            res = res[::-1]                    # Again Reverse The String
            nibble1 = res[0:len(res) // 2]     # Create Nibble1
            nibble2 = res[len(res) // 2:]        # Create Nibble2
            nibble1, nibble2 = nibble2, nibble1  # Swap Both Nibble

            binary = int(nibble1 + nibble2)      # Concat And Cast To Int

            decimal, i, n = 0, 0, 0

            while binary != 0:                   # Convert To Decimal Equivalent
                rem = binary % 10                   # Take Reminder
                decimal = decimal + rem * pow(2, i)  # Append The Reminder
                binary = binary // 10               # Divide The Number by 10
                i += 1
            print("Decimal Conversion Of", res, "=", decimal)     # Print Decimal Equivalent Of The Number


"""
    Main Class To Access The Above Class
"""
if __name__ == '__main__':
    decimal = DecimalToBinary()  # Create Object
    decimal.ConvertToBinary()      # Call Function
