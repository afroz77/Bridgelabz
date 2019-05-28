from util.Queue import Queue
import datetime as dt
from Week3.Commercial_Data_Process.File_Load import File_Load

"""
    Class TransactionQueue Having 2 Methods 
    1. Add Transaction
    2. Save Transaction
    
"""


class TransactionQueue:

    def __init__(self):
        self.queue = Queue()
        self.file_load = File_Load()
        try:
            self.transactions = self.file_load.Read_json("Transaction_Queue.json")
            for i in self.transactions:
                self.queue.enqueue(i)
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
        cr_date = dt.datetime.now()                         # Create DateTime Object To Store Transaction Time And Date
        cr_date = cr_date.strftime("%d/%m/%Y, %H:%M:%S")    # Format The Date And Time
        try:
            # Create newtransation Object And Assign Values
            newtransaction = {"transaction_type": tr_type, "company_name": company_name, "customer_name":customer_name,
                              "no_of_share": shares, "total_amount": total_amount, "date_time": cr_date}

            # Add To The Queue
            self.queue.enqueue(newtransaction)
        except :
            print("Undefined Error..")

    """
        Save Transaction Simply Save The Transaction
        In Json File
        
    """
    def SaveTransaction(self):
        try:
            temp = []                   # Declare One temp List
            size = self.queue.Size()    # Get The Size Of The Queue
            for i in range(size+1):     # Loop Through The size Of Queue
                temp.append(self.queue.dequeue())       # Append All Queue Data To The List
            self.file_load.Write_json(temp, "Transaction_Queue.json")   # Save List Data To The json
        except:
            print("Undefined Error..")


if __name__ == '__main__':
    pass
