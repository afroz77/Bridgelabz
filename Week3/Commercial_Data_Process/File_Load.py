import json

"""
    Class File Load Having 2 Method As Read_json And Write_json Methods
"""


class File_Load:

    def __init__(self):                     # Constructor
        pass

    def Read_json(self, file_name):         # Read Json Function Take File Name As Param To Read The File
        try:
            with open(file_name, 'r') as file:  # Open File In Read Mode
                return json.load(file)          # Return JSON Data To Caller
        except FileNotFoundError:               # Validation Error
            print("File Not Found.")

    def Write_json(self, data, file_name):         # Write Json Function Take Data To Write And File Name As Params
        try:
            with open(file_name, 'w') as file:       # Open File In Write Mode
                json.dump(data, file, indent=2)      # Writing Data In Json Format
                return True                          # If Write Then Return True
        except FileNotFoundError:                    # Validation Error
            print("File Not Found.")
            return False
