from Week1.Util import IsAnagram

"""
    Class Anagram Having Angramcheck() Function..
    
"""


class Anagram:
    """
        Function Anagramcheck() Ask Two Input Strings And Check Whether The Entered Strings Are Anagram Or not

    """
    def Anagramcheck(self):
        try:
            str1 = input("Enter First String : ")           # Ask For Entering First String
            str2 = input("Enter Second String : ")          # Ask For Entering Second String
            str1, str2 = IsAnagram(str1, str2)              # Pass Both Strings To IsAnagram Function
                                                            # Which Return Reverse Strings

            if str1 == str2:  # Comparing Both Strings If Equal Then Anagram
                print("\nStrings Are Anagram ")     # Print Message As Strings Are Anagram
            else:
                print("\nStrings Are Not Anagram ")  # Print Strings Are Not Anagram
        except ValueError:                          # Else Except Value Error
            print("Invalid Strings")                # Print Validation Error
            self.Anagramcheck()                     # Call Self


"""
    Main Class To Access Above Anagram Class Create Object And Call Functions
"""
if __name__ == '__main__':
    anagram = Anagram()         # Create Anagram Class Object
    anagram.Anagramcheck()      # Call Anagramcheck function
