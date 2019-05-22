from util.dsutil import readfile, updatefile, overwrite
from util.LinkedList import linkedlist
list = linkedlist()
try:
    word = readfile('test.txt')
    for item in word:
        list.addnode(item)
    print("Current List Is : ", end='')
    list.display()
    val = input("\nEnter Value To Search : ")
    if list.searchword(val):
        print("\nElement Found And Deleted From The File")
        word.remove(val)
        list.deletenode(val)
        overwrite(word, 'test.txt')
    else:
        print("\nElement Not Found And Added To The List")
        word.append(val)
        list.addnode(val)
        updatefile(val, 'test.txt')
    print("File Updated Successfully : ", end='')
    list.display()
except FileNotFoundError:
    print("File Not Found..!")