from Week1.Util import merge_sort

"""
    In This Method Declare One Array Ask User To Enter Array Element 
    And Pass It To The Util Function And Print The Array
    
"""

def MergeSort():
    try:
        n = int(input("Enter Array Length : "))  # Ask USer For Inout
        if not str(n).isnumeric():  # Validate The Input
            raise ValueError  # Raise Value Error
            return  # Return
        arr = [0 for i in range(n)]  # Declare Array
        for i in range(n):  # Loop Through Array Length
            num = int(input("Enter Next : "))  # Ask User For Array Element
            if not str(num).isdigit():  # Validate Array Element
                raise ValueError  # Raise Value Error
                return  # Return
            arr[i] = num  # Append Number To The Array

        print("Before Sorting : ", end='')
        for i in range(len(arr)):
            print(arr[i], '', end='')
        arr = merge_sort(arr)
        print("\n\nAfter Sorting : ", end='')
        for i in range(len(arr)):
            print(arr[i], '', end='')
    except ValueError:
        print("Invalid Error")
        MergeSort()


"""
    Main Method To Call The Function
"""
if __name__ == '__main__':
    MergeSort()

