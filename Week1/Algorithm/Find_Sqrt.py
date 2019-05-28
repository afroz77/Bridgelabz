from Week1.Util import Find_sqrt

"""
    The Square Root Class Have One Method To Take Input From User And Calculate The Square Root

"""


class Sqrt:

    def squareRoot(self):       # Function squareRoot
        try:                    # Error Handling
            c = int(input("Enter Number To Find SQRT : "))      # Ask User For Input Number
            while c <= 0:                                       # Check If The User Inputs Negative Number Or 0
                c = int(input("Enter Value > 0 : "))            # If Then Ask Recursively Till The Positive Number Not
            Find_sqrt(c)                                        # Call Find_sqrt() Function By Passing User Input
        except ValueError:                                      # Handling Error
            print("Enter Numeric Value Only..")                 # Print Error Message
            self.squareRoot()                                   # Call Self


"""
    Main Method To Create And Access The Class 
"""

if __name__ == '__main__':
    srrt = Sqrt()           # Create Object Of Sqrt Class
    srrt.squareRoot()       # Call squareRoot Function

