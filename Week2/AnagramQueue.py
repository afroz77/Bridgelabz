from Week1.Util import get_anagram, get_prime
from util.Queue import Queue
queue = Queue()

primearray = get_prime()            # Prime Numbers Array
anagrams = get_anagram(primearray)  # Anagram Numbers Array

for i in anagrams:                  # Add Elements Of Anagram Array In Queue
    queue.enqueue(i)

q_size = queue.Size()               # Calculate Size Of Queue

for i in range(q_size):             # Print Elements Of Queue
    print(queue.dequeue(), '', end='')