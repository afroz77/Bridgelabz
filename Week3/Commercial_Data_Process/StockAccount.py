from Week3.Commercial_Data_Process.Services import Services
flag = True
try:
    while flag:  # While Flag Is True Then Do The Same Process
        service = Services()  # Create Service() Class Object
        # Take User Choice 1 2 Or 3 As Shown If Message
        choice = input("\n1. Company Portal \n2. Customer Portal \n3. Exit\n\nSelect Option : ")
        if not choice.isnumeric():
            raise ValueError
        choice = int(choice)
        if choice == 1:  # Check The Input If 1 Then Go For Company
            # Take Choice For Company Transaction 1,2 Or 3
            ch = input("1. Add New Company \n2. Remove Company \n3. Print Company\n\nSelect Option : ")
            if not ch.isnumeric():
                raise ValueError
            ch = int(ch)
            if ch == 1:  # If Choice Is 1 Then
                service.Addcompany()  # Call Add New Company Function
            elif ch == 2:  # If Choice Is 2
                service.removecompany()  # Call Remove Company Function
            elif ch == 3:  # If Choice Is 3
                service.print(1)  # Call Print Function By Passing 1

        # Check The Input If 2 Then Go For Customer
        elif choice == 2:
            # Take Choice For Customer Transaction 1,2 Or 3 As Following Choices
            ch = input("\n1. Add New Customer\n2. Existing Customer\n3. Remove Existing Customer\n\nSelect Option : ")
            if not ch.isnumeric():
                raise ValueError
            ch = int(ch)
            if ch == 1:  # if choice is 1 then
                service.Addcustomer()  # call Addcustomer() Function
            elif ch == 2:  # If choice is 2 then
                service.Option()  # Call The Option() Function Which Will Ask For Authentications And Other Transaction
            elif ch == 3:
                service.removecustomer()  # if Choice Is 3 Then Call removecustomer() Function
            else:
                print("Invalid Choice Select From Above..")

        # Check The Input If 3 Then Go For Exit The Program
        else:
            print("Thank You Exiting....")  # Print Message
            flag = False  # Make Flag False
except ValueError:
    print("Invalid Input Enter Only Numeric Value ")
    flag = True

