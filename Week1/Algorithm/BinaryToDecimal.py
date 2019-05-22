from Week1.Util import Decimal_To_Binary
try:
    num=int(input("Enter a Number : "))
    while num<=0:
        num = int(input("Enter Possitive Number : "))
    temp = num
    res = Decimal_To_Binary(num)
    print("Binary Conversion Of", temp, "=", res)

    res=res[::-1]
    while len(res) <= 7:
        res += '0'
    res=res[::-1]
    nibble1=res[0:len(res)//2]
    nibble2=res[len(res)//2:]
    nibble1,nibble2=nibble2,nibble1

    temp=binary=int(nibble1+nibble2)

    decimal,i,n=0,0,0

    while binary != 0:
        rem=binary % 10
        decimal = decimal+rem*pow(2, i)
        binary = binary//10
        i += 1

    print("Decimal Conversion Of", res, "=", decimal)
except:
    print("Invalid Input ")