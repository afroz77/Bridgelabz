import math as m

"""
    Class Binary Search Calculate Binary Search Trees
    CountTree Method Takes A Number And Calculate The Possible Binary Trees And Print The Result 
    Formula To Calculate ((n*2)! / (n+1)! * n!)
"""

class BinarySearch:

    def countTree(self, number):
        num = int((m.factorial(number*2)) / (m.factorial(number+1) * m.factorial(number)))
        print("\nTotal Possible Binary Trees For Number", number, "Is :", num)


bs = BinarySearch()                  # Create Class Object
try:
    num = int(input("Enter Number To Find Binary Trees : "))  # Ask User To Input A number
    bs.countTree(num)                    # Call countTree Method
except ValueError:
    print("\nError : Invalid Input ")