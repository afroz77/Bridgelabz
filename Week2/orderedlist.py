from util.dsutil import readfile, updatefile, overwrite
from util.LinkedList import *
from array import *

lst = linkedlist()                            # Object Of Class LinkedList
arr = array('i', [])
try:
    print("Current List Is :", end='')
    arr = readfile('numberlist.txt')          # Reading File In List
    for i in arr:
        lst.sortlist(i)                       # Insert Data To Linked List
    lst.display()                             # Display List

    val = input("\nEnter a Number : ").strip()  # Get User Input
    if lst.searchword(val):                     # Search If Found
        lst.deletenode(val)                     # Delete Element
        arr.remove(val)                         # Update List
        overwrite(arr, 'numberlist.txt')        # Over Write The File
        print("\nElement Found And Deleted From The List")
    else:
        lst.sortlist(val)                               # Add New Element At Appropriate Position
        print("\nElement Not Found Added To The List")
        updatefile(val, 'numberlist.txt')               # Append That Element In Text File
    print("File Updated :", end='')
    lst.display()                                 # Display Updated list

except FileNotFoundError:
    print("\nFile Not Found..")                    # Print File Not Found Error
