from Week1.Util import Isprime

"""
    Calculate And Show The Prime Numbers Between Range 0 To 1000
"""


def Primenumbers():
    try:
        count = 1
        number = 2
        rng = int(input("Enter Range : "))
        if not str(rng).isnumeric():
            raise ValueError
            return
        while count < rng:
            res = Isprime(number)
            if res:
                print(number, '  ', end='')
            count += 1
            number += 1
    except ValueError:
        print("Invalid Error..")
        Primenumbers()


"""
    Main Method
"""

if __name__ == '__main__':
    Primenumbers()