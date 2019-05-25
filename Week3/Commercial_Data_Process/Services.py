from builtins import complex

from Week3.Commercial_Data_Process.File_Load import File_Load
"""
    Class Services Do The Following Operations On Company And Also On Customer Data
    1. Add New Customer
    2. Remove Existing Customer
    3. Add New Comapany
    4. Remove Existing Company 
    5. Print Company Data
    6. Print Customer Data
    7. Buy Share
    8. Sell Share
    
"""


class Services:        # Class Variables
    fl = File_Load()   # Object Of File Load Class
    c_key = None       # Variable To Store Key

    def __init__(self):
        pass

    def __init__(self):         # Override The Default Constructor

        self.customer_data = self.fl.Read_json("customer.json")         # Read Customer Data Passing File Name
        self.company_data = self.fl.Read_json("company.json")           # Read Company Data Passing File Name
        self.company_keys = list(self.company_data["company"].keys())  # Store Company Keys From Data Using Keys() Fun
        self.customer_keys = list(self.customer_data["customer"].keys())  # Store Customer Keys Customer Data

    # -------------------------- Add Customer Method ---------------------------------- #
    def Addcustomer(self):
        try:
            customer_name = input("Enter Customer Name : ")         # Take User Name  Input
            balance = input("Available Balance : ")                 # Available Cash
            shares = input("Available Shares : ")                   # Available Shares
            price = input("Enter Shares Price : ")                  # Share Price
            if not customer_name.isalpha() or not shares.isnumeric() or not balance.isnumeric() or not price.isnumeric():
                raise ValueError                        # Validate And Raise Error
        except ValueError:
            print("You Entered Wrong Data..")           # Print Validation Error
            self.Addcustomer()                          # Recursively Call Self
            return                                      # Return From Method
        else:
            ch = input("\nDo You Want To Save y/n : ")  # Ask Confirmation To Save
            if ch.upper() == "Y":
                if self.checkexist(customer_name, 2):   # Checking The User Already Exist
                    print("User Already Exist..")       # If True Then Print Message
                    self.Addcustomer()                  # Call Self Function
                else:
                    self.customer_data["customer"][customer_name.upper()] = ({  # Else Append New Customer Data
                        'name': customer_name,
                        'balance': balance,
                        'shares': shares,
                        'price': price,
                    })
                    if self.fl.Write_json(self.customer_data, "customer.json"):  # Save New Customer Data
                        print("Customer Added Successfully ")                # If Return True Then Print Message
                        self.c_key = None                                    # Update c_key To None
                        return                                          # Return From The Method
            else:
                print("You Cancelled The Process..")

    # --------------------------------- Add Company Method ------------------------------------------------

    def Addcompany(self):
        try:
            company_name = input("Enter Company Name : ")  # Take Company Name As Input
            balance = input("Available Balance : ")        # Available Balance
            shares = input("Available Shares : ")          # Available Shares
            price = input("Shares Price: ")                # Share Price
            if not company_name.isalpha() or not shares.isnumeric() or not balance.isnumeric() or not price.isnumeric():
                raise ValueError        # Validate All inputs
        except ValueError:              # Raise Validation Error
            print("You Entered Wrong Data..")
            self.Addcompany()            # Call To Self Method
            return
        else:
            ch = input("\nDo You Want To Save y/n : ")      # Take Confirmation To Save Company Data
            if ch.upper() == "Y":
                if self.checkexist(company_name, 1):        # Check Exist Company Name If Exist
                    print("Company Name Already Exist..")
                    self.Addcompany()                       # Call Self Method
                else:
                    self.company_data["company"][company_name.upper()] = ({   # Else Append New Data To Current Data
                        'name': company_name,
                        'balance': balance,
                        'shares': shares,
                        'price': price,
                    })
                    if self.fl.Write_json(self.company_data, "company.json"):  # Save The Company Data In Json File
                        print("Company Added Successfully ")                   # If Return True Then Print Message
                        self.c_key = None                                      # Update c_key To None
                        return                                                 # Return From The Method
            else:
                print("You Cancelled The Process..")

    # ---------------------------- Remove Customer Or Delete Existing Customer --------------------
    def removecustomer(self):
        try:
            customer_name = input("Enter Customer Name To Delete : ")       # Take Customer Name
            if not customer_name.isalpha():             # Validate Input For Symbols Or Special Char
                raise ValueError                        # True The Raise Value Error

        except ValueError:
            print("Invalid Input..")                # Print The Validation Message
        else:
            if self.checkexist(customer_name, 2):   # Check The Customer Name Exist Or Not If Exist
                ch = input("Do You Want To Delete y/n :")   # Then Ask For Confirmation
                if ch.upper() == "Y":
                    print("Record Deleted..")               # Print Message
                    del self.customer_data['customer'][self.c_key]  # Delete The Customer Data From List
                    self.fl.Write_json(self.customer_data, "customer.json")     # Save Updated Data To The Json
                    self.c_key = None                           # Update c_key As None
                else:
                    print("Cancelled Operation.")
            else:                                          # If CheckExist Return False It Means The Record Not Found
                print("Record not Found..")                # Print The Message

    # ------------------------- Remove Company Or Delete Existing Company -------------------------------
    def removecompany(self):
        try:
            company_name = input("Enter Company Name To Delete : ")  # Take Company Name As Input
            if not company_name.isalpha():              # Validate The Input And Raise ValueError
                raise ValueError
        except ValueError:
            print("Invalid Input..")                    # Print Validation Message
        else:
            if self.checkexist(company_name, 1):        # Check Exist Company Name If True
                ch = input("Do You Want To Delete y/n :")   # Ask For Confirmation
                if ch.upper() == "Y":
                    print("Record Deleted..")               # Delete Message
                    del self.company_data['company'][self.c_key]        # Delete The Data From Company List
                    self.fl.Write_json(self.company_data, "company.json")   # Write Updated Data To Json
                    self.c_key = None                               # Update c_key To None
                else:
                    print("Cancelled Operation.")
            else:                                         # If Check Exist Return False Then  Print Record Not Found
                print("Record not Found..")

    """
    
    ------------------------Check Exist Method Take 2 Params As Data And ch -----------------------------------
     
    Note : Data Can Contains Company Name Or Customer Name
           ch Can Contains 1 or 2 
           if ch is 1 Then Check The Data In Company Data
           if ch is 2 Then Check The Data In Customer Data
    """

    def checkexist(self, data, ch):
        if ch == 1:                        # Checking The Data In Company Data
            for key in self.company_keys:  # Loop in Company Keys
                if str(key).upper() == str(data).upper():       # If Data Match Then
                    self.c_key = key                            # Update c_key with match Company key
                    return True                                 # Return True
            return False                                        # Else Return False
        else:                              # If ch ==2 Then Check The Data In Customer Data
            for key in self.customer_keys:  # Loop In Customer Data
                if str(key).upper() == str(data).upper():   # Check The Data If Match
                    self.c_key = key                        # Update c_key With Match Customer Key
                    return True                              # Return True
            return False                                      # Return False

    # --------------------- Get Company  Method Return The Company Name As Key----------------------
    def get_company(self, ch):             # Take user choice
        count = 1                          # Initialize Count
        for key in self.company_keys:      # Loop Through Keys
            if count == ch:                # If Choice And Count Match Then Return Than Key
                return key
            count += 1                      # Else Update count By 1

    # ----------------------- Get Customer Method Return Customer Name as Key----------------------
    def get_customer(self, ch):           # Take User Choice
        count = 1                         # Initialize The Count as 1
        for key in self.customer_keys:    # Loop through The Customer Keys
            if count == ch:               # If Count And Choice Equal
                return key                # Return The Key
            count += 1                    # Else Update Count

    """
        Option Method Ask User To Do User Operations Like Buy Sell Or Print The Current Customer Data 
        1. Buy Shares
        2. Sell Shares
        3. Print Customer Details       
        
    """
    def Option(self):
        try:
            customer_name = input("Enter Customer Name : ").upper()    # Take USer Input As Customer Name
            if not customer_name.isalpha():                             # Validate Input if Not Alphabets
                raise ValueError                                        # Raise Value Error
        except ValueError:                                              # Except The Value Error
            print("Enter Valid Input ")             # Print Validation Message
        else:
            if self.checkexist(customer_name, 2):    # Check Customer Exist Or Not If True
                ch = int(input("\n1. Buy Share\t\t2. Sell Share\t\t3. Print Data\n\nSelect Option : "))
                if ch == 1:
                    self.print(1)
                    ch = int(input("\nSelect Company To Buy: "))
                    com_name = self.get_company(ch)
                    self.buy(com_name, customer_name)
                elif ch == 2:
                    self.print(1)
                    ch = int(input("\nSelect Company To Sell: "))
                    com_name = self.get_company(ch)
                    self.sell(com_name, customer_name)
                elif ch == 3:
                    print("\n************************ CUSTOMER DETAILS **************************\n")
                    print("Customer Name \t\t Total Share \t\t Total Amount \t\t Price")
                    print(self.customer_data["customer"][customer_name]['name'], "    \t\t     ",
                          self.customer_data["customer"][customer_name]['shares'], "    \t\t    ",
                          self.customer_data["customer"][customer_name]['balance'], " \t\t        ",
                          self.customer_data["customer"][customer_name]['price'])
                else:
                    print("Wrong Choice")
                    self.Option()
            else:
                print("Not Found")
                self.Option()

    def buy(self, company_name, customer_name):
        try:
            company_share = int(self.company_data['company'][company_name]['shares'])
            company_amount = int(self.company_data['company'][company_name]['balance'])
            customer_amount = int(self.customer_data['customer'][customer_name]['balance'])
            customer_share = int(self.customer_data['customer'][customer_name]['shares'])
            company_share_price = int(self.company_data['company'][company_name]['price'])

            shares = int(input("Enter Share To Buy : "))
        except ValueError:
            print("Enter Numeric Value For Share")
            return
        else:
            shares = int(shares)
            if shares * company_share_price <= customer_amount and company_share >= shares:
                self.company_data['company'][company_name]['balance'] = company_amount + int(shares * company_share_price)
                self.company_data['company'][company_name]['shares'] = company_share - shares
                self.customer_data['customer'][customer_name]['shares'] = customer_share + shares
                self.customer_data['customer'][customer_name]['balance'] = customer_amount - int(shares * company_share_price)
                print("Shares Buy From", company_name, "Cash Deducted By", shares*company_share_price,
                      "Current Share Is", customer_share + shares)
                self.fl.Write_json(self.company_data, "company.json")
                self.fl.Write_json(self.customer_data, "customer.json")
            else:
                print("Insufficient Cash")

    def sell(self, company_name, customer_name):
        try:
            company_share = int(self.company_data['company'][company_name]['shares'])
            company_amount = int(self.company_data['company'][company_name]['balance'])
            customer_share_price = int(self.customer_data['customer'][customer_name]['price'])
            customer_amount = int(self.customer_data['customer'][customer_name]['balance'])
            customer_share = int(self.customer_data['customer'][customer_name]['shares'])
            shares = int(input("Enter Share To Sell : "))
        except ValueError:
            print("Enter Numeric Value For Share")
            return
        else:
            shares = int(shares)
            if shares * customer_share_price <= company_amount and customer_share >= shares:
                self.company_data['company'][company_name]['balance'] = company_amount - int(shares * customer_share_price)
                self.company_data['company'][company_name]['shares'] = company_share + shares
                self.customer_data['customer'][customer_name]['shares'] = customer_share - shares
                self.customer_data['customer'][customer_name]['balance'] = customer_amount + int(shares * customer_share_price)
                print("Shares Sold To", company_name, "Cash Received", shares * customer_share_price,
                      "Current Balance Is", customer_amount + shares * customer_share_price)
                self.fl.Write_json(self.company_data, "company.json")
                self.fl.Write_json(self.customer_data, "customer.json")
            else:
                print("Insufficient Cash")

    def print(self, ch):
        if ch == 1:
            print("\n************************ COMPANY DETAILS **************************\n")
            print("Company Name \t\t Total Share \t\t Total Amount \t\t Price")
            count = 0
            for key in self.company_keys:
                count += 1
                print(count, self.company_data["company"][key]['name'], "    \t\t",
                      self.company_data["company"][key]['shares'], "    \t\t    ",
                      self.company_data["company"][key]['balance'], " \t\t    ",
                      self.company_data["company"][key]['price'])
        else:
            print("\n************************ CUSTOMER DETAILS **************************\n")
            print("Customer Name \t\t Total Share \t\t Total Amount \t\t Price")
            count = 0
            for key in self.customer_keys:
                count += 1
                print(count, self.customer_data["customer"][key]['name'], "    \t\t",
                      self.customer_data["customer"][key]['shares'], "    \t\t    ",
                      self.customer_data["customer"][key]['balance'], " \t\t        ",
                      self.customer_data["customer"][key]['price'])

