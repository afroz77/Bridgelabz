
try:
    row = int(input("Enter No Of Rows : "))
    col = int(input("Enter No Of Columns : "))
    arr = [[0 for i in range(col)] for j in range(row)]
    print("Enter", row * col, "Elements :")

    for i in range(row):
        for j in range(col):
            x = int(input("Enter Array Element: "))
            arr[i][j] = x

    for i in range(row):
        for j in range(col):
            print(arr[i][j], '', end='')
        print()
except ValueError:
    print("\nInvalid Input Enter Integers..!")