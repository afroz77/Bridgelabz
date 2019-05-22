from Week1.Util import sortarraylist,binarysearch # Import Functions From Util File
import array

arr=array.array('i', [])
n=int(input("Enter Array Length : "))
for i in range(n):
    arr.append(int(input("Enter Next : ")))
arr = sortarraylist(arr)
val = int(input("Enter Value To Search : "))
result = binarysearch(0, len(arr)-1, val, arr)
if result != 1:
    print("Element Found ")
else:
    print("Element Not Found ")