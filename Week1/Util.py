from math import *


def calc_change(rupees):

    arr = (1000, 500, 100, 50, 20, 10, 5, 2, 1)
    notes = 0
    for i in range(len(arr)):
        if rupees // arr[i] > 0:
            print("\nNote Of", arr[i], "Is", rupees // arr[i])
            notes += rupees // arr[i]
            rupees = rupees % arr[i]
    print("\nNumber Of Notes Are : ", notes)

# ---------------------------  Print Harmonic Series  ------------------------------------- #


def print_series(num):
    res = 0.0
    for i in range(1, num+1):      # For Loop For Printing Nth Series
        if i == int(num) :
            res = res+float(1/i)
            print("1/" + str(i) + " = ", end='')    # Prints Ith Series With Equal Sign If I And N Equal
        else:
            res = res + float(1 / i)
            print("1/" + str(i) + " + ", end='')    # Else Prints Ith Series With Addition Sign
    print(round(res, 2))


# -------------------------  Find Roots Of Quadratic Equation  ---------------------------------- #


def find_roots(a, b, c):

    delta = (b * b) - (4 * a * c)       # Calculate Delta With Given Formula
    sq_root = sqrt(abs(delta))          # Calculate Square Root
    root1 = (-b + sq_root) / (2 * a)    # Calculate Root 1
    root2 = (-b - sq_root) / (2 * a)    # Calculate Root 2

    print("Root 1 : ", round(root1,2))  # Print Root 1
    print("Root 2 : ", round(root2,2))  # Print Root 2


# ---------------------------  calculate Euclidean Distance  ------------------------------------- #

# takes x and y as parameter and return distance


def calculateDistance(x, y):

    distance = sqrt(x ** 2 + y ** 2)  # Calculating Distance By Given Formula
    return distance                   # Return Distance between x And Y


# ---------------------------  Calculate Square Root Of Given Number  ------------------------------------- #


def Find_sqrt(c):
    t = c                                     # Initialize t With c
    t = c / t
    while abs(t - c / t) > (1e-15 * t):       # Loop Through  Checking Condition By Given Formula And Calculate Average
        t = (c / t + t) / 2.0
    print("Square Root Of", c, "Is", round(t, 2))


# --------------------------------- Calculate Day Of Week  -------------------------------------------- #

def DayOfWeek(day, month, year):

    list1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] # List Of Days In a Week
    y0 = year - (14 - month) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + 31 * m0 // 12) % 7                         # All Formula's Are Given In Question
    print("\nThe day Of Week Is :", list1[d0])                  # Print Day Of Week


# ---------------------------------  Check Palindrome -------------------------------------------- #

# Check Palindrome Or Not Takes One Integer Value And Return Reverse Number

def Ispalindrome(num):
    reverse = 0
    while num > 0:                   # Loop For Reversing Number
        rem = num % 10               # Calculating Reminder
        reverse = (reverse*10)+rem   # Appending Reminder To Reverse
        num = num//10
    return reverse                   # Return Reverse String


# -----------------------------------  Check Prime -------------------------------------------- #

# IsPrime Function Takes a Number And Return True If It Is Prime Else Return False

def Isprime(num):
    for i in range(2, num):    # Loop For Checking Prime
        if num % i == 0:         # If Reminder Is 0 Then Not Prime
            return False      # Return False
            break             # Break The Loop
    else:
        return True


# Get Prime Function Returns The Prime Numbers Between Range Of 0 1000

def get_prime():
    count = 1
    number = 2
    primearray = []             # blank array for storing prime numbers
    while count <= 1000:        # loop for checking prime numbers between range 0 to 1000
        res = Isprime(number)   # check the number is prime or not
        if res:
            primearray.append(number)           # if prime then add it in array
        count += 1
        number += 1
    return primearray                       # return prime array


# Get Anagram Function Returns The Prime Numbers That Are Anagram Between Range Of 0 1000

def get_anagram(primearrray):

    anagramarray=[]                         # blank array for storing anagram prime
    for i in range(len(primearrray) - 1):   # external loop for 1st element
        str1 = sorted(str(primearrray[i]))  # store first number and sort
        for j in range(i + 1, len(primearrray)):   # internal loop from i+1 to length of array
            str2 = sorted(str(primearrray[j]))     # second number and sort
            if str1 == str2:                       # compare both numbers if equal store in array
                anagramarray.append(primearrray[i]) # add in array
    return anagramarray                             # return anagram array


# -------------------------- Check The String Is Anagram Or Not ------------------------------- #


def IsAnagram(str1, str2):

    while len(str1) != len(str2):                      # Checking The Strings Are Equal Or Not
        print("Both Strings Should Be Equal In Length ")
        str1 = input("Enter First String : ")
        str2 = input("Enter Second String :")

    str1 = sorted(str1)                            # Sorting Strings
    str2 = sorted(str2)

    return str1, str2


def IsAnagram1(str1, str2):

    if len(str2) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False

# --------------------------------- Sort Array And List -------------------------------------- #

# Sort Array Function Takes An Array Or List As Input And Return Sorted Array Or Array


def sortarraylist(arr):
    try:
        for i in range(len(arr)-1):              # Outer Loop For First Element
            for j in range(i+1, len(arr)):        # Inner Loop For Next Element
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]  # Swapping Array element
        return arr
    except :
        print("Error : Invalid Type Array")

# ------------------------------------ Sort String ----------------------------------------- #


# Sort String Method Take a String And Return Sorted String

def sortstring(str):
    ln=len(str)
    for i in range(ln-1):
        for j in range(i+1, ln):
            if str[i] > str[j]:
                str[i], str[j] = str[j], str[i]   # swapping alphabets
    print(str)
    return str


# -------------------------------------  Bubble Sort  ----------------------------------------- #

def bubble_sort(arr):

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr = swap(i, j, arr)
    return arr
# ------------------------------------- Binary Search ----------------------------------------- #

# Function  To Search Item Binary Form
# Takes l r value to Search And 1 Array
# Return 1 If Not Found


def binarysearch(l, r, val, arr):

        while l <= r:
            middle = (l + r) // 2
            if arr[middle] == val:
                return True
            elif arr[middle] < val:
                l = middle + 1
            else:
                r = middle - 1
        return False

# -------------------------------- Insertion Sort ---------------------------------------- #

# Insertion Sort function
# Take An Array And Return Sorted Array


def insertionsort(arr):

    for i in range(1, len(arr)):        # Loop in Range Upto 1 to Array Length
        key = arr[i]                    # Initialize Key As Array Of i
        j = i-1                         # Initialize J Value As i-1
        while j >= 0 and key < arr[j]:  # Loop For Sorting Element In Array
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key                  # Assign Array Of j as Key
    return arr

# ----------------------------------- Merge  Sort ---------------------------------------- #


def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr)//2         # calculate Mid Value

        L = arr[0:mid]            # Dividing Array In Right As R And Left As L
        R = arr[mid:]

        merge_sort(L)           # Recursively Calling Function For Left Array
        merge_sort(R)           # Recursively Calling Function For Right Array

        i = j = k = 0

        # Merging Array

        while i < len(L) and j < len(R):

            if L[i] < R[j]:              # Checking left and right Array If Less Then
                arr[k] = L[i]              # Assign The Value Of Left To Original Array
                i += 1
            else:                        # If Larger Than Left Then
                arr[k] = R[j]            # Assign The Value Of Right To Original Array
                j += 1
            k += 1

        while i < len(L):                # Copying The Remaining Elements Of L If Any Remains
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):                # Copying The Remaining Elements Of R If Any Remains
            arr[k] = R[j]
            j += 1
            k += 1

    return arr                           # Return Sorted Array

# ------------------------------- Swap Two Numbers In Array  ---------------------- #

# function swap takes i,j as index and array
# return Swapped array


def swap(i, j, arr):

    arr[i],arr[j] = arr[j],arr[i]
    return arr

# -------------------------------- Search Word In The Given List --------------------- #

# Search Word From a List
# Take List And Word To Search
# Return 1 If Found Else 0

def searchword(list,word):

    l = 0
    r = len(list)-1
    while l <= r:
        mid = (l+r)//2
        if list[mid].casefold() == word.casefold():
            return 1
        elif list[mid].casefold() < word.casefold():
            l = mid+1
        else:
            r = mid-1
    else:
        return 0

# -------------------------------- Temprature Conversion ------------------------------------ #

# Temprature Conversion Conversion Method Takes Temprature and n value


def TempratureConversion(temp, n):
    if n == 0:                                   # n is 0 then convert to fehrenhiet
        fahrenhiet = (temp*9/5)+32                     # formula to convert the temprature
        print("Celsius To Fahrenhiet = ", round(fahrenhiet, 2), 'F')
    if n == 1:                                   # n is 1 then convert to Celsius
        celsius = (temp-32)*5/9                     # formula to convert the temprature
        print("\nFahrenhiet To Celsius = ", round(celsius, 2), 'C')

# ---------------------------------- Calculate Payment Of The Month -------------------------- #

def IsLeap(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

def CalcPayment(P, Y, R):
                        # p = principle amount
    r = R / (12 * 100)  # r = rate of interest
    n = 12 * Y          # y = years
    payment = (P * r) / (1 - (1 + r) ** (-n))
    print("Monthly Payment Is = ", round(payment, 2))
    return payment

# --------------------------- Number Conversion Decimal To Binary -------------------------- #

# Function Take One Number And Return Binary Equivalent Number


def Decimal_To_Binary(num):
    try:
        res = ''
        num = int(num)
        while num != 0:
            rem = num % 2  # Reminder
            num = num // 2
            res += str(rem)  # Append Reminder To String
        return res[::-1]  # Reverse The String And Return It
    except ValueError:
        print("Invalid Value")


def to_decimal(number):

    while len(str(number)) < 8:
        number = number + str(0)
    s3 = number[4:8]
    s4 = number[0:4]
    swap = s3 + s4
    b = str(swap)
    return int(b)