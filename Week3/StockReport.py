from util.oop_util import Stock

obj = Stock()
n = int(input("\nEnter No Of Shares To Add : "))
for i in range(n):
    obj.addreport()
obj.showreport()

