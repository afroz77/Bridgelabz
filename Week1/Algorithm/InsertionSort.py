from Week1.Util import insertionsort
from array import*

n=int(input("Enter Array Length : "))
arr=[0 for i in range(n)]

for i in range(n):
    arr[i]=(int(input("Enter Next : ")))

print("Before Sorting : ",end='')
for i in range(len(arr)):
    print(arr[i],' ',end='')

print("\nAfter Sorting : ",end='')
arr=insertionsort(arr)

for i in range(len(arr)):
    print(arr[i],' ',end='')