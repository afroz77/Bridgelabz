from  Week1.Util import TempratureConversion
ch="Y"
while ch.upper()=="Y":
    n=int(input("Enter Value 0 Or 1 (0 For C To F And 1 For F To C) : "))
    if n==0:
        temp=float(input("Enter Temprature In Celsius : "))
    if n==1:
        temp = float(input("Enter Temprature In Fahrenhiet : "))
    TempratureConversion(temp,n)
    ch=input("Do You Want To Convert Another y / n : ")
print("Bye..")