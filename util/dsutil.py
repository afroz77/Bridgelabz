from builtins import enumerate
from math import modf

import numpy                                    # import numpy module for declaring 2d Array
from Week1.Util import IsAnagram1,IsLeap
from array import *                             # import array module for declaring 1D array
from util.LinkedList import linkedlist          # import linkedlist class
from util.Queue import Queue                    # import Queue Class
from util.Stack import Stack                    # import Stack Class


def updatestack(data):

    stack1 = Stack()
    stack2 = Stack()
    lista = []
    listb = []
    for i in range(5):
        lista.append(stack1.pop())
        listb.append(stack2.pop())

    ind = lista.index(data)
    listb[ind] = listb[ind] + 1

    for i in range(len(lista)):
        stack1.push(lista[i])

    for i in range(len(listb)):
        stack2.push(listb[i])


"""
    Readfile Method Take FileName And Read The File And Return The List
"""


def readfile(filename):
    with open(filename, 'r') as File:     # Open File As test.txt
        lst = File.read().split()      # Read File And Store In List
        File.close()
    return lst


"""
    UpdateFile Method Append The Element In The Current File
"""


def updatefile(word, filename):
    f = open(filename, 'a')          # open file file in append mode
    f.write(" %s " % word)           # write the word
    f.close()                       # close the file
           

"""
    OverWrite Method Takes A List And Filename To Over Write File Content
"""


def overwrite(lst, filename):
    f = open(filename, 'w')         # Open File In write mode
    for item in lst:                # Loop Through All Items in List
        f.write("%s " % item)       # Write In the File
    f.close()                       # Close The File


# Function Take One String And Check Whether The Giver Equation Is Balanced Or Not


def BalanceParanthesis(Val):

    stack = Stack()             # Create Object Of Class Stack
    for i in Val:               # Loop In String For Each Alphabet
        if i is '(' or i is '{' or i is '[':       # Check The Value Of i If It Open Bracket Then Push In Stack
            stack.push(i)
        elif i is ')' and stack.peak() is '(' or i is '}' and stack.peak() is '{' or i is ']' and stack.peak() is '[':
            stack.pop()            # Else Check The Last Element Of The Stack And ith Element Of String
                                   # If One Of Them Is True Then Pop The Element Else Continue The Loop
    if stack.Isempty():
        return True
    else:
        return False


""" PrintTwoDarray Function Takes An Array as Argument And Check The Anagram Primes And Not Anagram numbers 
    And Print The 2D Array
"""
class Twodarray:

    def __init__(self):
        self.anagramarray = numpy.full((200, 2), 0)     # Initialize 2D Array With Static Value

    def printtwoDarray(self, primearray):

        count = 0
        flag = True

        for i in range(len(primearray)):                # Loop Through All The Element In Array
            for j in range(len(primearray)):            # J Loop For Pointing Next Array Element
                if i == j:
                    continue
                flag = True
                if IsAnagram1(str(primearray[i]), str(primearray[j])):   # Check Two Numbers Are Anagram
                    self.anagramarray[count][0] = primearray[i]          # If Anagram Then Store In Anagram Array 0
                    count += 1
                    flag = False                                         # Flag False
                    break
            if flag:                                                     # Flag is True Is Not Anagram
                self.anagramarray[i][1] = primearray[i]                  # Store That Element Anagram Array In 1

        for row in range(200):                                  # Print The 2D Array
            for col in range(2):
                if self.anagramarray[row][col] == 0:            # If Zero Then Continue
                    continue
                else:
                    print(int(self.anagramarray[row][col]), ' | ', end='')  # Else Print Array Value
            print()


"""
    Hash Table Class Creates 11 Linked list Object From Index 0 To 10
    read_hashfile Method Read The File Content And Store In Array
    sortlist Method Just Add And Sort The Data In Linked List
    rem Variable Calculate The Remainder As Index To Store Number
    User_Input Method Simply Ask User For Input Number 
    Searchword Method Check The Number Is Present in Current List If Present Then Delete That Number
    SortList Method Add The Number At The Specific Index In The list     
    
"""


class Hashtable:
    def __init__(self):
        self.lst = []                     # Initialize One Empty List
        self.arr = array('i', [])         # Initialize One Empty Array
        for i in range(11):
            self.lst.append(linkedlist())   # Create 11 Objects Of Type LinkedList

    def read_hashfile(self):
        l = readfile('hashtable.txt')               # Reading File
        for i in l:
            self.arr.append(int(i))                 # Append File Content In Array
        for i in range(len(self.arr)):
            rem = int(self.arr[i]) % 11
            self.lst[rem].sortlist(self.arr[i])     # Create Sorted Linked List

    def user_input(self):

        n = int(input("Enter a Number : "))         # Ask User For Input
        rem = n % 11                                # Calculate Remainder As Index Of Array
        if self.lst[rem].searchword(n):             # Search The Number If Found
            self.lst[rem].deletenode(n)             # Delete The Number
            self.arr.remove(n)
            overwrite(self.arr, 'hashtable.txt')    # Update File Content
            print("\nFound At", int(rem), "And Deleted ")
        else:
            print("\nNot Found Added At :", rem)    # If not Found
            self.lst[rem].sortlist(n)               # Add To Specific Index
            updatefile(n, 'hashtable.txt')          # Append Text File

    def display(self):
        for i in range(11):                         # Display Hash Table Content
            if self.lst[i].Isempty():
                print(i, ": ")
                continue
            print(i, ': ', end='')
            self.lst[i].display()
            print()


class Calender:

    """
        __init__ Method To Initialize Name Of The Days, month Names, Month days And 2D Array

    """
    def __init__(self):
        self.day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        self.month_name = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUNE', 'JULY', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.cal_array = numpy.array((6, 7))

    """
        This Method Store The Month Days And and Print The Calender In 2D Format
        Takes year And month As parameters
    """

    def Show_Cal(self, year, month):
        d = 1
        m = month
        y = year
        if IsLeap(year):
            self.month_days[1] = 29
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m)//12) - 2
        start_day = (d + x + 31 * m0 // 12) % 7               # it gives start Day Of the month

        print("\n----------", self.month_name[month-1], "-", year, "-----------\n")  # Print Calender Heading
        for i in range(7):
            print(self.day[i], end='  ')                # print Days Of The Week
        print()

        date = 1
        for i in range(6):                              # store calender date in array
            for j in range(7):
                if date <= self.month_days[m-1]:        # check the date less than the month days
                    if i == 0 and j < start_day:        # check if i==0 and j < start day
                        continue                        # then continue the loop
                    self.cal_array[i][j] = date         # else store than date in array position
                    date += 1                           # update date by 1

        for i in range(6):                              # print the calender array in formatted output
            for j in range(7):
                if self.cal_array[i][j] == 0:
                    print(end='     ')
                    continue
                if self.cal_array[i][j] < 10:
                    x = int(self.cal_array[i][j])
                    print(x, end='    ')
                else:
                    x = int(self.cal_array[i][j])
                    print(x, end='   ')
            print()

    """
        This Method Store Calender using Queue
        Take year and month parameter
        And Display The Calender For The Month
    """

    def Show_Cal_Queue(self, year, month):

        queue = Queue()             # Queue class object
        d = 1
        m = month
        y = year
        if IsLeap(year):             # check if leap year
            self.month_days[1] = 29  # than update month days value
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        start_day = (d + x + 31 * m0 // 12) % 7     # calculate start day

        print("\n-------------", self.month_name[month - 1], "-", year, "--------------\n")  # print heading

        for i in range(7):                      # print week days
            print(self.day[i], end='   ')
        print()

        date = 1
        for i in range(6):                      # store the dates in queue
            for j in range(7):
                if date <= self.month_days[m - 1]:  # check the date less than the month days
                    if i == 0 and j < start_day:    # check if i==0 and j < start day
                        queue.enqueue(0)
                        continue
                    queue.enqueue(date)              # else store than date in Queue position
                    date += 1                        # update the date

        try:
            for i in range(6):  # print the calender in formatted output
                for j in range(7):
                    if queue.Size() >= 0:
                        x = int(queue.dequeue())
                        print(str(x).ljust(2), end='    ')
                print()
        except:
            print()
