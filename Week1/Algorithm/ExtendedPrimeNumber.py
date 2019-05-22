from Week1.Util import Isprime,Ispalindrome,get_anagram
from array import*

count=1
number=1
primeArray=array('i',[])

print("\nPrime Numbers : ", end='')
while count <= 1000:
    res = Isprime(number)
    if res:
        print(number,' ',end='')
        primeArray.append(number)
    count += 1
    number += 1

print("\n\nPrime Numbers That Are Palindrome : ", end='')
for i in range(len(primeArray)):
    if primeArray[i] == Ispalindrome(primeArray[i]) :
        print(primeArray[i], ' ' ,end='')

print("\n\nPrime Numbers That Are Anagram :", end='')

anagrams=get_anagram(primeArray)
for i in anagrams:
    print(i, ' ', end='')
