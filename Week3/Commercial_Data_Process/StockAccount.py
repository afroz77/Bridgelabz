from Week3.Commercial_Data_Process.Services import Services
flag = True
while flag:
    service = Services()
    choice = int(input("\n1. Company Portal \n2. Customer Portal \n3. Exit\n\nSelect Option : "))
    if choice == 1:
        ch = int(input("1. Add New Company \n2. Remove Company \n3. Print Company\n\nSelect Option : "))
        if ch == 1:
            service.Addcompany()
        elif ch == 2:
            service.removecompany()
        elif ch == 3:
            service.print(1)
    elif choice == 2:
        ch = int(input("\n1. Add New Customer\n2. Existing Customer\n3. Remove Existing Customer\n\nSelect Option : "))
        if ch == 1:
            service.Addcustomer()
        elif ch == 3:
            service.removecustomer()
        else:
            service.Option()
    else:
        flag = False
