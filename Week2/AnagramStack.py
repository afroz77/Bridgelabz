from Week1.Util import get_anagram,get_prime
from util.Stack import Stack
stack = Stack()
primearray = get_prime()                # Prime Number Array
anagrams = get_anagram(primearray)      # Array Of Anagram Numbers

for i in anagrams:
    stack.push(i)                       # Push All Anagrams In Stack

l_size = stack.size()                   # Calculate Size Of Stack

while l_size >= 0:
    print(stack.pop(), '', end='')      # Print Stack Elements
    l_size -= 1
