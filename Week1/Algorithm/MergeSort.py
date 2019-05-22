from Week1.Util import merge_sort
from array  import *
arr = [12, 11, 13, 5, 6, 7, 0]
type(arr)
print("Before Sorting : ", end='')
for i in range(len(arr)):
    print(arr[i], '', end='')
arr = merge_sort(arr)
print("\n\nAfter Sorting : ", end='')
for i in range(len(arr)):
    print(arr[i], '', end='')
