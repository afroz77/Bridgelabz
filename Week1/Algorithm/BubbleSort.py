from Week1.Util import swap,bubble_sort
from array import *

"""
    Function BubbleSort To Sort The Array
    Ask User For Enter Array Length And Array Elements
"""


def BubbleSort():
    try:
        arr = array('i', [])            # Declare One Array
        n = int(input("Enter Array Length : "))     # Ask User For Input
        if not str(n).isnumeric():                  # Validate User Input Is Numeric Or Not If Not
            raise ValueError                        # Raise Value Error
            return                                  # Return
        for i in range(n):                          # Else Loop Through The Length Of Array
            num=int(input("Enter Element : "))      # Ask User To Enter Array Element
            if not str(num).isnumeric():            # Validate The User Input If Not Numeric
                raise ValueError                    # Raise Value Error
                return                              # Return Method
            arr.append(num)                         # Else Append The Number To Array
        arr = bubble_sort(arr)                      # Sort The Array By Passing To The Function
        print('\nSorted Array Is : ', end='')
        for i in range(n):                      # Printing Sorted Array
            print(arr[i], ' ', end='')
    except ValueError:                          # except The Value Error
        print("Invalid Input : ")               # Print Error Message
        BubbleSort()                            # Call Self


"""
    Mian Method To Call Above Function
"""
if __name__ == '__main__':
    BubbleSort()    # Function Call

