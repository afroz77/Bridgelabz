from Week1.Util import sortarraylist, binarysearch    # Import Functions From Util File
import array

"""
    Class Binary Search Having One Function As Search 
    To Search An Element In The Array
    
"""


class Binarysearch:

    """

       Function Search Ask User To Enter Array Length And Array Elements
       After Entering Value Print The Result

    """

    def Search(self):
        try:
            arr = array.array('i', [])          # Declare An Array
            n = input("Enter Array Length : ")  # Ask User To Enter Array Length
            if not n.isnumeric():               # Validate The Value If Not Numeric
                raise ValueError                # Then Raise Value Error
                return                          # Return Method
            for i in range(int(n)):                  # Loop Through The Array Length And
                num=input("Enter Next : ")      # Ask User To Enter Array Element
                if not num.isnumeric():         # Validate The Input Is Not Numeric
                    raise ValueError            # Raise Value Error
                    return                      # Return From Method
                arr.append(int(num))                 # Else Append Data
        except ValueError:                      # Accept Value Error
            print("Invalid Input")              # Print Valllidation Message
            self.Search()                       # Call Self Method
        else:
            arr = sortarraylist(arr)            # Sort Array
            val = int(input("Enter Value To Search : "))  # Ask User To Enter Value To Search In Given Array
            result = binarysearch(0, len(arr) - 1, val, arr)        # Pass The Array To binarysearch Function
            if result:                                  # If Function Return True
                print("Element Found ")                 # Print Element Found
            else:
                print("Element Not Found ")             # Else Print Element Not Found


"""
    Main Class To Access Above Declare Class
"""
if __name__ == '__main__':
    binary_search = Binarysearch()      # Create Object Of Class
    binary_search.Search()              # Call Function
