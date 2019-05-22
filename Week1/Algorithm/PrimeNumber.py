from Week1.Util import Isprime
count=1
number=1
while count<=1000:
    res=Isprime(number)
    if(res):
        print(number)
    count+=1
    number+=1