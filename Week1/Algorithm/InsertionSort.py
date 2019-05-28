from Week1.Util import insertionsort

"""
    InsertionSort Function Ask User To Enter Array Length And Array Element
    Validate The Both Array Length And Array Element For Numeric Value
    After Getting Array Then Pass Array To Util Function InsertionSort And 
    Print Sorted Array
"""


def InsertionSort():
    try:
        n = int(input("Enter Array Length : "))     # Ask USer For Inout
        if not str(n).isnumeric():                  # Validate The Input
            raise ValueError                        # Raise Value Error
            return                                  # Return
        arr = [0 for i in range(n)]                 # Declare Array
        for i in range(n):                          # Loop Through Array Length
            num = int(input("Enter Next : "))       # Ask User For Array Element
            if not str(num).isnumeric():            # Validate Array Element
                raise ValueError                    # Raise Value Error
                return                              # Return
            arr[i] = num                          # Append Number To The Array

    except ValueError:                              # Handle Error
        print("Enter Numeric Value..")
        InsertionSort()                             # Call Self

    else:
        print("Before Sorting : ", end='')          # Print The Unsorted Array That User Enters
        for i in range(len(arr)):
            print(arr[i], ' ', end='')

        print("\nAfter Sorting : ", end='')         # Print The Array After Sorting
        arr = insertionsort(arr)
        for i in range(len(arr)):
            print(arr[i], ' ', end='')


"""
    Main Method To Call Above Function
"""
if __name__ == '__main__':
    InsertionSort()     # Call Function


