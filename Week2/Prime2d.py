import numpy                                    # Import Numpy Package
from Week1.Util import get_prime


class Twodarray:

    def __init__(self):                         # Init Method Which Initialize One 2D Array With Values 0
        self.array=numpy.zeros((10, 30))

    """ twodprime Function Which Takes One Array
        Checks Primes Between Range And Prints In 2d Format 
    """

    def twodprime(self, primearray):
        rnge = 100
        col = row = 0

        for i in primearray:                        # Loop Through Whole Array
            if i > rnge:                              # check if block value Is less than i
                row += 1                            # if true then increment row by by 1
                col = 0
                rnge += 100                           # block value by 100
            self.array[row][col] = i                # else Store that number in array
            col += 1                                # increment column value by one

        bl = 100
        st = '000'

        for row in range(10):                       # Loop For Rows
            print(st, '-', bl, "| ", end='')
            for col in range(30):                   # loop For Columns
                if self.array[row][col] == 0:
                    continue
                print(int(self.array[row][col]), ' | ', end='')  # Printing Array Value
            st = bl
            bl += 100
            print()


primearray = get_prime()      # Get Prime Numbers In The Range Of 0 to 1000
t = Twodarray()             # Creating Object Of Class
t.twodprime(primearray)     # Calling Function With Passing The Array Of Prime Numbers