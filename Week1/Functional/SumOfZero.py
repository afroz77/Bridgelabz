from array import *
ar = array('i', [])
ar1 = array('i', [])
try:
    n = int(input("Enter Array Length : "))
    for i in range(n):
        val = int(input("Enter Next Value: "))
        ar.append(val)
    count = 0
    for i in range(len(ar) - 2):
        for j in range(i + 1, len(ar) - 1):
            for k in range(j + 1, len(ar)):
                if ar[i] + ar[j] + ar[k] == 0:
                    print(ar[i], ar[j], ar[k], " = 0 ")
                    count += 1
    print("\nTotal Triplets Are : " + str(count))
except ValueError:
    print("\nInvalid Input Enter only Integers..!")