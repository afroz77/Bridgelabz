import json               # Import JSON Library
import sys                # Import Sys Module
from re import search     # import Regex Search Method

"""
    Services Class Do Following Operations In Address Book 
    1. Create New Json File
    2. Open A Existing Json File
    3. Save Data In The Json File
    4. Save As Option Text Or Json
    5. Add New Person Details In Address Book 
    6. Delete A Person From Address Book
    7. Update Data Of Existing Person In Address Book
    8. Lastly Print The File Content 
    
"""


class Services:             # Class Services
    def __init__(self):
        self.lst = {}       # Initialize lst Variable As Dictionary
        self.file_name = None      # File Name As none

# Create Method Create The New Json File

    def Create(self):
        temp = {'data': []}    # Initial Data Format For Storing In File
        try:
            file_name = input("Enter File Name : ")     # Take Input File Name
            if file_name.isdigit():                     # Validate File Name
                print("File Name Should Contain Only Stings..")
                self.Create()
                return
            else:
                with open(file_name+".json", 'w') as file:      # Open File And Create New File With Given Name
                    json.dump(temp, file, indent=2)             # Write Json Format In File
                    file.close()                                # Close File
                    print("File Created Successfully..")
        except NameError:
            print("Name Should Contain Only Stings..")

# This Methos Opens The Existing File Or If File Is Not Available Then Create New File

    def Open(self):
        try:
            file_name = input("Enter File Name : ")         # Take Input For File Name
            with open(file_name+".json", 'r') as file_data: # Open File With Extension .json In Read Mode
                if file_data is not None:                   # Check If File Id Empty Or Not
                    self.lst = json.load(file_data)         # Read JSON Data in Initialize Variable
                else:
                    print("File Empty.")
            self.file_name = file_name+".json"
        except FileNotFoundError:                           # Validation Error Message
            print("File Not Found ")
            self.Open()

# This Method Save The All Data In The Current Opened File

    def Save(self):
        try:
            with open(self.file_name, 'w') as data:     # Open The File In Write Mode
                json.dump(self.lst, data, indent=2)     # Write Content In JSON Using json.dump Method
                data.close()                            # Close The File
            print("\nData Saved Successfully..")
        except FileNotFoundError:                       # Print Validation Message
            print("File Not Found..")

# This Method Save The File As Text Format Or In JSON Format

    def Saveas(self):

        file_name = input("Enter File Name With Extension text or json ")  # Take File Name With Extension
        j = search(".json", file_name)                        # Search For .json Extension Using Regex Search() Method
        txt = search(".txt", file_name)                       # Search For .txt Extension Using Regex Search() Method
        sel = 0
        if txt is not None and txt.group() == ".txt":         # Check If The Extension Is txt
            sel = 1
        if j is not None and j.group() == ".json":            # Check If The Extension Is json
            sel = 2
        if sel == 1:
            with open(file_name, 'w') as data:                # If .txt Then Create New TEXT File
                data.write(str(self.lst))
                print("Text File Created..")
                data.close()
        elif sel == 2:                                        # If .json Then Create New JSON File
            with open(file_name, 'w') as data:
                json.dump(self.lst, data)
                print("JSON File Created..")
                data.close()
        else:
            print("Invalid Extension")

# This Method Add New Person To The Address Book

    def addnew(self):
        addnewrecord = {}  # Create A Dictionary

        try:
            first_name = input("Enter First Name : ")       # Taking User Inputs
            last_name = input("Enter Last Name : ")
            mobile_num = input("Enter Mobile Number : ")
            address = input("Enter Address : ")
            city = input("Enter City Name : ")
            state = input("Enter State Name : ")
            zip_code = input("Enter Zip Code : ")

            if not first_name.isalpha() or not last_name.isalpha() or not mobile_num.isnumeric() \
                    or not address.isalpha() or not city.isalpha() or not state.isalpha()\
                    or not zip_code.isnumeric():        # Validate All The Entered values
                raise ValueError

        except ValueError:                              # Print The Error Message
            print("\nYou Entered Wrong Data : ")
            self.addnew()                               # Call Self Add Method
        else :
            if not self.Validate(first_name, last_name):        # Else Validate The First Name And Last Name In
                                                                # Existing File By Passing To Validate()
                print("\nDuplicate Data Please Enter Valid Details ")   # Print Message For Duplication
                self.addnew()                                   # Call Self
                return                                          # Return
            else:
                addnewrecord['first_name'] = first_name         # Else Adding Data To The Dictionary
                addnewrecord['last_name'] = last_name
                addnewrecord['mobile_number'] = mobile_num
                addnewrecord['address'] = address
                addnewrecord['city'] = city
                addnewrecord['state'] = state
                addnewrecord['zip_code'] = zip_code
                self.lst["data"].append(addnewrecord)           # Append New Data To The Current Data
                self.Save()                                     # Calling Save() Function
                self.Print()                                    # Print The Updated Address Book
# This Method Delete The Record From Address Book

    def Delete(self):
        first_name = input("Enter First Name : ")               # Take First Name
        last_name = input("Enter Last Name : ")                 # Take Last Name
        for i in range(len(self.lst["data"])):                  # Loop Through In Existing Record
            # Check If Record Available Or Not If Found Then Delete That Record From Address Book
            if str(self.lst["data"][i]['first_name']).casefold() == first_name.casefold() and \
                    str(self.lst["data"][i]['last_name']).casefold() == last_name.casefold():
                print("Record Deleted Deleted")
                del self.lst["data"][i]                    # Updating The List Of Person
                self.Save()                                # Save Updated File
                self.Print()                               # Print The Address Book
                return                                     # Return The Method
        else:
            print("\nNo Record Found ")                    # If Name Not Match Then Print The Message

# This Method Simply Print The Address Book Details

    def Print(self):
        try:

            if len(self.lst["data"]) >= 1:  # Check The File Length If Not Empty Then Print The Address book
                print(
                    "\n************************************* ADDRESS BOOK DETAILS ************************************\n")
                print("First Name\t\tLast Name\t\tMobile Number\t\tAddress\t\tCity\t\tState\t\tZipCode")
                for i in range(len(self.lst["data"])):  # Loop Through All The Records
                    print(self.lst["data"][i]['first_name'], "\t\t\t", self.lst["data"][i]['last_name'], "\t\t\t",
                          self.lst["data"][i]['mobile_number'], "\t\t", self.lst["data"][i]['address'], "\t\t",
                          self.lst["data"][i]['city'], "\t\t", self.lst["data"][i]['state'], "\t\t",
                          self.lst["data"][i]['zip_code'])
            else:
                print("No Record Found..")  # Print Message
                choice = input("Do You Want To Add New Record..? y/n ")  # Ask To Add New Record
                if choice.upper() == "Y":  # If Yes Then
                    self.addnew()  # Call The Addnew() Method
                else:
                    sys.exit()  # Exit The Program
        except:
            print("File Is Empty")

    def Sort(self):
        print(self.lst)
        self.lst = sorted(self.lst)
        print(self.lst)

# This Method validate The First Name And Last Name For Adding New Record
    def Validate(self, first_name, last_name):   # First Name And Last_name As Parameter
        try:
            for i in range(len(self.lst["data"])):  # Loop Through The list
                if self.lst["data"][i]['first_name'] == first_name and self.lst["data"][i]['last_name'] == last_name:
                    return False  # If The Name Found Then Return False
            return True  # Else Return True
        except:
            print("File Is Empty Or No Record Found")

# This Method Update The Address Book Record Of A Particular Person
    def Update(self):
        try:
            flag = update = False               # Declare 2 Variable And Initialize False
            if len(self.lst["data"]) >= 1:      # Check The File Is Empty Or Not
                first_name = input("Enter First Name : ")       # Take First Name And Last Name For Authentication
                last_name = input("Enter Last Name : ")
                for i in range(len(self.lst["data"])):          # Loop Through The List And Check If The User Exist
                    if str(self.lst["data"][i]['first_name']).casefold() == first_name.casefold() and \
                       str(self.lst["data"][i]['last_name']).casefold() == last_name.casefold():
                            flag = True                         # If Exist Then Update The Flag As True
                            break                               # Break The loop
                if flag:                              # Check If Flag Is True Then Ask To Update Options
                    print("What Do You Want To Update : 1. City 2. Address 3. State   4.Mobile Number  5.Zip_Code ")
                    choice = int(input("Enter Choice From Above : "))  # Take Input
                    if choice == 1:                               # If 1 Then Update The City Only
                        city = input("Enter New City Name :")     # Take New Input
                        self.lst["data"][i]['city'] = city        # OverWrite The New Value With Old One
                        update = True                             # Update The update Variable To True
                    elif choice == 2:                             # If 2 Then Update The Address Only
                        address = input("Enter New Address :")      # Take New Input
                        self.lst["data"][i]['address'] = address    # OverWrite The New Value With Old One
                        update = True                               # Update The update Variable To True
                    elif choice == 3:                               # If 2 Then Update The State Only
                        state = input("Enter New State :")          # Take New Input
                        self.lst["data"][i]['state'] = state        # OverWrite The New Value With Old One
                        update = True                               # Update The update Variable To True
                    elif choice == 4:                                   # If 2 Then Update The Mobile Number Only
                        mobile = input("Enter New Mobile :")            # Take New Input
                        self.lst["data"][i]['mobile_number'] = mobile   # OverWrite The New Value With Old One
                        update = True                                   # Update The update Variable To True
                    elif choice == 5:                               # If 2 Then Update The Xip Code Only
                        zip = input("Enter New Zip :")              # Take New Input
                        self.lst["data"][i]['zip_code'] = zip       # OverWrite The New Value With Old One
                        update = True                               # Update The update Variable To True
                    else:
                        print("Invalid Input..")                    # Print Invalid Input
                        update = False
                        self.Print()                                # Print
                else:
                    print("Enter Integer Only.")                    # Validation For Integer
                    self.Update()                                   # Call Self Method
            else:
                print("Enter Valid Name ")                          # Message To Enter Valid Name
                self.Update()                                       # Call Self Method
        except:
            print("Error : Invalid Input ")

        if update:                                          # If update Is True
            self.Save()                                     # Save The Updated Record
            self.Print()                                    # Print The Address Book

