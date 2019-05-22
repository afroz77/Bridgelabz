from Week1.Util import Decimal_To_Binary
ch='Y'
while ch.upper()=="Y":
    num=int(input("Enter a Number : "))
    temp=num
    res=Decimal_To_Binary(num)
    print("Binary Conversion Of", temp, "=", res)
    ch=input("\nDo You Want To Convert Another y/n : ")
print("Bye..")

