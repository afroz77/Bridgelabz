from Week1.Util import searchword,sortarraylist

"""
    In This Call Declare One Constructor in The Constructor Reading The Text File 
    And Assign Content To The list
    And The Function Will Take User Input And Search The Word.
    
"""


class SearchWord():
    def __init__(self):                 # Constructor
        with open('test.txt', 'r') as f:    # Reading File From Present Directory
            self.lst = f.read().split()     # Assign The Content To The List

    def SearchWord(self):
        try:
            lst = sortarraylist(self.lst)   # Sort The List By Calling And Passing The List To Function
            ch = "Y"                        # Initialize As Y
            while ch.upper() == 'Y':        # Till Y Execute The Following
                word = input("Enter Word To Search In List : ")     # Ask User To Enter Value To Search
                if not word.isalpha():              # Validate The Input Isalpha
                    raise ValueError                # Raise Value Error
                    return                          # Return
                result = searchword(lst, word)      # Store Return Value True Or False
                if result == 1:                     # If 1 then True
                    print(word.upper(), "Is Found In List ")    # Print The Word Found Message
                else:
                    print(word.upper(), "Is Not Found In List ")     # Else Print Word Not Found Message
                ch = input("\nDo You Want To Search Another y/n :")     # Ask To Find Another
            print("Bye..")
        except ValueError:              # except ValueError
            print("Invalid Input..")       # Print Message
            self.SearchWord()               # Call Self


"""
    Main Method To Create Object And Call The Functions
    
"""

if __name__ == '__main__':
    sw = SearchWord()           # Create The Object Of Class
    sw.SearchWord()             # Call The Method

