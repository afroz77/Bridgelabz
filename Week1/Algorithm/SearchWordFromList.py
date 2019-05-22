from Week1.Util import searchword,sortarraylist
with open('test.txt') as f:
    lst = f.read().split()
lst = sortarraylist(list)
ch = "Y"
while ch.upper() == 'Y':
    word = input("Enter Word To Search In List : ")
    result = searchword(list, word)
    if result == 1:
        print(word.upper(), "Is Found In List ")
    else:
        print(word, "Is Not Found In List ")
    ch = input("\nDo You Want To Search Another y/n :")
print("Bye..")