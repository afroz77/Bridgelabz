from Week3.AddressBook.Services import Services
import sys

try:
    s1 = Services()           # Create Class Object
    s1.Open()                 # Call Open() Function To Open The File For Following Operations
    choice = int(input("Choose Option From Following\n1. Add New Record \n2. Delete Record \n3. Update Address Book \n"
                       "4. Print Address Book\n5. Create New File.\n6. Quit\n"
                       "Enter Choice : "))
    if choice == 1:  # If Choice Is 1 Then Call addnew() Function
        s1.addnew()
    elif choice == 2:  # If Choice Is 2 Then Call Delete() Function
        s1.Delete()
    elif choice == 3:  # If Choice Is 3 Then Call Update() Function
        s1.Update()
    elif choice == 4:  # If Choice Is 4 Then Call Print() Function
        s1.Print()
    elif choice == 5:  # If Choice Is 5 Then Call Create() Function
        s1.Create()
    elif choice == 6:  # If Choice Is 6 Then Call Exit From The Program
        print("Exited.")
        sys.exit()  # Call System Exit Method

except FileExistsError:
    print("Error : Invalid ")
