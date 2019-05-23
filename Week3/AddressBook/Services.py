import json
from re import search


class Services:
    def __init__(self):
        self.lst = {}
        self.file_name = None

    def Create(self):
        try:
            file_name = input("Enter File Name : ")
            if file_name.isdigit():
                print("File Name Should Contain Only Stings..")
                self.Create()
                return
            else:
                f = open(file_name+".json", 'w')
                f.close()
                print("File Created Successfully..")
        except NameError:
            print("Name Should Contain Only Stings..")

    def Open(self):

        try:
            file_name = input("Enter File Name To Open..")
            with open(file_name+".json", 'r') as file_data:
                print("File Open..")
                self.lst = json.load(file_data)
            self.file_name = file_name
            print(self.lst)
        except FileNotFoundError:
            print("File Not Found ")
            self.Open()

    def fetch(self):
        print(self.file_name)
        try:
            with open(self.file_name+".json", 'r') as file_data:
                self.lst = json.load(file_data)
        except FileNotFoundError:
            print("File Not Found ")
            self.Open()
        print(self.lst)

    def Save(self):
        print(self.file_name)
        try:
            with open(self.file_name+".json", 'w') as data:
                json.dump(self.lst, data)
                data.close()
            print("\nData Saved Successfully..")
        except FileNotFoundError:
            print("File Not Found..")

    def Saveas(self):

        file_name = input("Enter File Name With Extension text or json ")
        j = search(".json", file_name)
        txt = search(".txt", file_name)
        sel = 0
        if txt is not None and txt.group() == ".txt":
            sel = 1
        if j is not None and j.group() == ".json":
            sel = 2
        if sel == 1:
            with open(file_name, 'w') as data:
                data.write(str(self.lst))
                print("Text File Created..")
                data.close()
        elif sel == 2:
            with open(file_name, 'w') as data:
                json.dump(self.lst,data)
                print("JSON File Created..")
                data.close()
        else:
            print("Invalid Extension")

    def addnew(self):
        addnewcustomer = {"data": {}}

        first_name = input("Enter First Name : ")
        last_name = input("Enter Last Name : ")
        mobile_num = input("Enter Mobile Number : ")
        address = input("Enter Address : ")
        city = input("Enter City Name : ")
        state = input("Enter State Name : ")
        zip_code = input("Enter Zip Code : ")

        addnewcustomer["data"]['first_name'] = first_name
        addnewcustomer["data"]['last_name'] = last_name
        addnewcustomer["data"]['mobile_num'] = mobile_num
        addnewcustomer["data"]['address'] = address
        addnewcustomer["data"]['city'] = city
        addnewcustomer["data"]['state'] = state
        addnewcustomer["data"]['zip_code'] = zip_code

        self.lst.update(addnewcustomer)
        print(self.lst)

        ch = int(input("Do You Want To Save."))
        if ch == 1:
            self.Save()
        else:
            return

