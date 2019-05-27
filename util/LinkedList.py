from util.Node import Node

"""
    Linked List Class Do The Following Operations
    1. Add Node
    2. Delete Node
    3. Search Node
    4. Add To Start 
    5. Sort The Linked List
    6. Print Linked list
    . ete
"""


class linkedlist :

    def __init__(self):
        self.head = None              # Init Method To Initialize Head Node None

# This Method Add New To The Last

    def addnode(self, data):

        newnode = Node(data)                    # Create NewNode Of Type Class Node
        if self.head is None:                   # List Is Empty Then Add To Start
            self.head = newnode
        else:                                   # Traverse Till The End
            tempnode = self.head
            while tempnode.next is not None:
                tempnode = tempnode.next
            tempnode.next = newnode             # Add Newnode At The End Of The List

#  Display Method Print The Linked list

    def display(self):
        tempnode = self.head

        if tempnode is None:  # TempNode Is None Print List Is Empty
            print("List Is Empty..")
            return
        while tempnode.next is not None:  # Traversing The List
            print(tempnode.data, ' ', end='')  # Print Content Of The List
            tempnode = tempnode.next  # Points To The Next
        print(tempnode.data, ' ', end='')  # Prints Last Element

#    This Method Add Node To The Start Of The Linked List

    def addtostart(self, data):
        newnode = Node(data)
        newnode.next = self.head  # Point Newnode To Head Node
        self.head = newnode  # Assign Newnode As Head Node

#    This Method Sort The Linked list Also Take Data And Add To The Appropriate Position

    def sortlist(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            tempnode = self.head
            if tempnode.data > data:
                newnode.next = tempnode
                self.head = newnode
            else:
                prevnode = self.head
                while tempnode is not None:
                    if tempnode.data > data:
                        newnode.next = prevnode.next
                        prevnode.next = newnode
                        return
                    prevnode = tempnode
                    tempnode = tempnode.next
                prevnode.next = newnode

#    This Method Search The Data in Linked list
#    If The Data Found Return True
#   Else Return False

    def searchword(self, data):
        self.display()
        tempnode = self.head
        print(data)
        while tempnode is not None:
            if tempnode.data == data:
                return True
            tempnode = tempnode.next
        return False

    # This Method Match The Data And Delete The Node

    def deletenode(self, data):
        prevnode = tempnode = self.head
        if tempnode.data == data:
            self.head = tempnode.next
        else:
            while tempnode.data != data:
                prevnode = tempnode
                tempnode = tempnode.next
            prevnode.next = tempnode.next

#    This Method Takes Index And Delete The Particular Node At That Index

    def delete_by_index(self, index):

        if index is 0:
            self.head = self.head.next
            return

        currentnode = self.head
        for i in range(index):
            prevnodenode = currentnode
            currentnode = currentnode.next
        prevnodenode.next = currentnode.next

#  This Method Return The Data Of Last Node

    def pull_last(self):
        tempnode = prevnode = self.head
        if tempnode is None:
            return -1
        if tempnode.next is None:
            self.head = None
        while tempnode.next is not None:
            prevnode = tempnode
            tempnode = tempnode.next
        prevnode.next = None
        return tempnode.data

# This Method Returns The Data Of The First Method

    def pull_first(self):

        tempnod = self.head
        if tempnod is None:
            return -1
        self.head = tempnod.next
        return tempnod.data

# This Method Return The Data Of The Last Node

    def getLast(self):
        tempnode = self.head
        if tempnode is None:
            return -1
        while tempnode.next is not None:
            tempnode = tempnode.next
        return tempnode.data

#    This Method Checks The List Is Empty Or Not
#    If Empty Return True Else Return False

    def Isempty(self):
        if self.head is None:
            return True
        else:
            return False

# This Method Returns The Size Of The Linked List

    def Size(self):
        count = 0
        tempnode = self.head
        while tempnode.next is not None:
            count += 1
            tempnode = tempnode.next
        return count

    def get_by_index(self, index):
        tempnode=self.head
        for i in range(index):
            tempnode = tempnode.next
        return tempnode.data

