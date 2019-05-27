from util.Queue import Queue
import datetime as dt
from Week3.Commercial_Data_Process.File_Load import File_Load


class TransactionQueue:

    def __init__(self):
        self.queue = Queue()
        self.file_load = File_Load()
        self.transactions = self.file_load.Read_json("Transaction_Queue.json")
        for i in self.transactions:
            self.queue.enqueue(i)

    def AddTransaction(self, tr_type, company_name, customer_name, shares, total_amount):
        cr_date = dt.datetime.now()
        cr_date = cr_date.strftime("%d/%m/%Y, %H:%M:%S")
        newtransaction = {"transaction_type": tr_type, "company_name": company_name, "customer_name":customer_name,
                          "no_of_share": shares, "total_amount": total_amount, "time": cr_date}
        self.queue.enqueue(newtransaction)

    def SaveTransaction(self):
        temp = []
        size = self.queue.Size()
        for i in range(size+1):
            temp.append(self.queue.dequeue())
        self.file_load.Write_json(temp, "Transaction_Queue.json")


if __name__ == '__main__':
    tq = TransactionQueue()
    tq.AddTransaction("Sell", "Google", "Afroz", 10, 200)
    tq.SaveTransaction()

