from util.oop_util import Stock
obj = Stock()
obj.showreport()
try:
    n = int(input("\nEnter No Of Shares Wants To Add : "))
    for i in range(n):
        obj.addreport()
    obj.showreport()
except NameError:
    print("Invalid Input.")
