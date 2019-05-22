from Week1.Util import swap,bubble_sort
from array import *
try:
    n=int(input("Enter Array Length : "))
    arr=array('i',[])

    for i in range(n):
        print("Enter Element",i+1,' : ',end='')
        arr.append(int(input()))

        arr=bubble_sort(arr)

    print('\nSorted Array Is : ', end='')
    for i in range(n):
        print(arr[i],' ',end='')
except:
    print("Invalid Input : ")