from util.Stack import Stack
import datetime as dt
from Week3.Commercial_Data_Process.File_Load import File_Load

"""
        Class TransactionStack Having 2 Methods 
        1. Add Transaction
        2. Save Transaction
    
    """


class TransactionStack:

    def __init__(self):
        self.stack = Stack()                # Create Object Of Stack Class
        self.file_load = File_Load()        # Create Object Of File_Load Class
        try:
            self.transactions = self.file_load.Read_json("Transaction_Stack.json")  # Read JSON
            for i in self.transactions:             # Loop Through All JSON Data
                self.stack.push(i)                  # Push All Data In The Stack
        except FileNotFoundError:
            print("File Not Found..")
    """
            AddTransaction Method Takes 5 params
            tr_type : Type Of Transaction BUY Or SELL
            company_name : Name Of The Company
            customer_name : Name Of The Customer
            shares : Number Share That Has Been Sell Or Buy
            total_amount : total Amount Of The Transaction

        """

    def AddTransaction(self, tr_type, company_name, customer_name, shares, total_amount):
        cr_time = dt.datetime.now()                     # Create DateTime Object
        cr_time = cr_time.strftime("%d/%m/%Y, %H:%M:%S")    # Format The Date And Time

        try:
            # Create And Assign  newtransaction
            newtransaction = {"transaction_type": tr_type, "company_name":  company_name,
                              "customer_name": customer_name, "no_of_share": shares,  "total_amount": total_amount,
                              "date_time": cr_time}

            # Push new Transaction In The Stack
            self.stack.push(newtransaction)
        except:
            print("Undefined Error..")

    """
            Save Transaction Simply Save The Transaction
            In Json File

    """
    def SaveTransaction(self):
        try:
            temp = []                   # Declare One temp List
            size = self.stack.size()    # Get The Size Of The Queue
            for i in range(size+1):      # Loop Through The size Of Queue
                temp.append(self.stack.pop())       # Append All Queue Data To The List
            self.file_load.Write_json(temp, "Transaction_Stack.json")    # Save List Data To The json
        except:
            print("Undefined Error..")


if __name__ == '__main__':
    ts = TransactionStack()

