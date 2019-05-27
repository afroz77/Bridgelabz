from Week3.Commercial_Data_Process.File_Load import File_Load
from util.LinkedList import linkedlist


class CompanyShareWithLinkedList:
    def __init__(self):
        self.list = []
        self.customer_list = linkedlist()
        self.company_list = linkedlist()
        self.file_load = File_Load()
        self.company_data = self.file_load.Read_json("Company.json")
        for i in self.company_data:
            self.company_list.addnode(i)

    def add_new_company(self):
        """
            reading company data from company json file
            creating new company json data and then add into company linked list
            Update company json file After Adding

        """

        try:
            company_name = input("Enter company name : ").strip().upper()
            no_of_share = input("Enter number of share : ").strip()
            price = input("Enter share per price : ").strip()
            balance = input("Enter balance amount : ").strip()
            if not company_name.isalpha() or not no_of_share.isnumeric() or not price.isnumeric() or not balance.isnumeric():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return

        new_company = {"name": company_name, "data": {"no_of_share": no_of_share,
                                                      "price": price,
                                                      "balance": balance}}
        flag = True
        for i in self.company_data:
            if i['name'] == company_name:
                print("Duplicate Data Please Enter New Data")
                flag = False
                self.add_new_company()
        if flag:
            print("New Company Added To The List")
            self.company_list.addnode(new_company)
            self.save()

    def remove_company(self):
        """
        reading company data from json file and maintain in company linked list
        take company name and then find in company linked list
        update company json file after deletion

        """
        try:
            company_name = input("Enter company name : ").strip().upper()
            if not company_name.isalpha():
                raise ValueError
        except ValueError:
            print("You have entered wrong data.")
            return
        for i in range(self.company_list.Size()+1):
            if self.company_data[i]['name'] == company_name:
                self.company_list.delete_by_index(i)
                print("Record Deleted..")
                self.save()
                break
        else :
            print("\nNo Record Found..")

    def save(self):
        size = self.company_list.Size()
        for i in range(size + 1):
            self.list.append(self.company_list.pull_first())
        self.file_load.Write_json(self.list, "Company.json")

    def print(self):
        size = self.company_list.Size()
        for i in range(size+1):
            self.list.append(self.company_list.pull_first())
        print("Company Name\tNo Of Shares\t Price\t Balance ")
        for i in self.list:
            print(i['name'], "\t   ", i['data']['no_of_share'], "\t\t    ", i['data']['price'], "\t"
                  , i['data']['balance'])

# Main method


if __name__ == "__main__":
    while True:
        obj = CompanyShareWithLinkedList()
        try:
            choice = int(input("\n1. Add New Company\n2. Remove Company\n3. Print\n4. Exit\n\nEnter Choice : "))
            if choice == 1:
                obj.add_new_company()
            elif choice == 2:
                obj.remove_company()
            elif choice == 3:
                obj.print()
            else:
                print("Exit")
                break
        except ValueError:
            print("Enter Number Only")


