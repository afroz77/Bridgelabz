from util.dsutil import BalanceParanthesis
try:
    val = input("Enter A Equation : ")
    res = BalanceParanthesis(val)
    if res:
        print("\nThe Equation Is Balanced.")
    else:
        print("\nThe Equation Is Not Balanced.")
except ValueError:
    print("Invalid Input..")