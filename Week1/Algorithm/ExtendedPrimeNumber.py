from Week1.Util import Isprime,Ispalindrome,get_anagram
from array import*

"""
    Class PrimeNumber Use To Show All Prime Numbers Between 0 To 1000 And Also Show 
    The Anagram Prime And Palindrome Prime
"""


class PrimeNumber:
    """
        Return The Array Of All Prime Numbers Between Range 0 To 1000

    """
    def primenumbers(self):
        count = 1          # Initialize Counter As 1
        number = 2         # Initialize Number As 2 Because 1 Is Not Prime Nor
        primeArray = array('i', [])     # Declare One Empty Array
        print("\nPrime Numbers : \n  ", end='')
        while count <= 1000:            # While Loop Till The Number Reach 1000
            res = Isprime(number)       # Check The Number Is Prime Or Not
            if res:                     # If Prime
                print(number, ' ', end='')  # Print The Number
                primeArray.append(number)   # Append To The Array
            count += 1                      # Update Count By 1
            number += 1                     # Update number By 1
        return primeArray                   # Return Final Array

    """
        This Function Get The Prime Array By Calling Above Function And Check In That Array Palindrome And Anagram
        And Finally Print The All Prime All Palindrome And Anagram Numbers 
    
    """
    def primenumber(self):
        try:
            primeArray = self.primenumbers()  # Call Function And Sore The Array Of Prime Numbers

            # Print The Anagram Prime Numbers

            print("\n\nPrime Numbers That Are Anagram : \n  ", end='')
            anagrams = get_anagram(primeArray)        # Call The Function And Store The Array Of Anagram Primes
            for i in anagrams:                        # Print All Anagram Prime By Loop In Array
                print(i, ' ', end='')

            # Print The Palindrome Prime Numbers
            print("\n\nPrime Numbers That Are Palindrome : \n  ", end='')
            for i in range(len(primeArray)):
                if primeArray[i] == Ispalindrome(primeArray[i]):
                    print(primeArray[i], ' ', end='')

        except ValueError:
            print("Invalid Input.")
            self.primenumber()


"""
    Main Method To Access Above Class And Functions
"""

if __name__ == '__main__':
    prime = PrimeNumber()           # Create Object
    prime.primenumber()             # Call The Function

