from Week1.Util import DayOfWeek

"""
    Class DayOfWeek Have One Function As dayofweek()
    
"""


class DayWeek:
    """
        Function dayofweek() Ask User To Enter Day, Month And Year
        Then Pass To Util Function And Print The Result

    """
    def dayofweek(self):
        try:
            day = int(input("Enter Day : "))          # Get Input Day Value
            if not str(day).isnumeric() or day > 31:  # Validate The Day Value Not Greater Than 31 And Numeric Also
                raise ValueError                      # Raise Value Error
                return                                # Return

            month = int(input("Enter Month : "))          # Get Input Month Value
            if not str(month).isnumeric() or month > 12:  # Validate The Month Value Not > Than 12 And Numeric Also
                raise ValueError                          # Raise Value Error
                return                                    # Return
            year = int(input("Enter Year : "))              # Get Input Year Value
            if not str(year).isnumeric() or len(str(year)) < 4:  # Validate Year Length Not < Than 4 And Numeric Also
                raise ValueError                                # Raise Value Error
                return                                          # Return
            DayOfWeek(day, month, year)                         # Call Util Function DayOfWeek
        except ValueError:                                      # except The Error
            print("\nInvalid Input Enter Valid Data ")          # Print Error Message
            self.dayofweek()                                    # Call Self


"""
    Main Function To Create Object And Access The Of Above Class's Function
"""
if __name__ == '__main__':
    dow = DayWeek()       # Create Object
    dow.dayofweek()         # Call The Function
