from util.LinkedList import linkedlist


class Stack:
    def __init__(self):
        self.stack = linkedlist()

    def push(self, data):                   # Add Node To The Last
        self.stack.addnode(data)

    def pop(self):                          # Pop The Last Itm From The List
        return self.stack.pull_last()

    def peak(self):                         # Peak Recently Added Item
        return self.stack.getLast()

    def size(self):                         # Return Size Of The Stack
        return self.stack.Size()

    def Isempty(self):                      # Check The Stack Is Empty
        return self.stack.Isempty()