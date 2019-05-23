import json


class Stock:
    def __init__(self):
        self.ls = []
        try:
            with open('StockReport.json', 'r') as f:
                file_data = json.load(f)

            for i in file_data:
                self.ls.append(i)
        except :
            print("No Shares Report Available Add New Shares ")

    def addnew(self):
        dec = {"share_name": "",
               "share_price": "",
               "no_of_shares": "",
               "total_shares": ""}

        share_name = input("Enter Name : ")
        no_of_shares = input("Enter No Of Shares : ")
        share_price = input("Enter Share Price : ")

        dec["share_name"] = share_name.upper()
        dec["share_price"] = share_price
        dec["no_of_shares"] = no_of_shares
        dec["total_shares"] = int(no_of_shares) * int(share_price)

        return dec

    def addreport(self):
        dt = self.addnew()
        self.ls.append(dt)
        f = open('StockReport.json', 'w')
        json.dump(self.ls, f)

    def showreport(self):
        print("\nSr.No Company Name  Price No Of Shares Total Shares\n")
        count = 0
        for i in self.ls:
            count += 1
            print(count,"\t ", i['share_name'],'\t   ',i['share_price'],'\t ', i['no_of_shares'],'\t\t   ', i['total_shares'])