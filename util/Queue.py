from util.LinkedList import linkedlist

class Queue:
    def __init__(self):
        self.queue = linkedlist()

    def enqueue(self, data):              # Add New Element To The List And Return
        self.queue.addnode(data)

    def dequeue(self):                    # Pop The First Element And Return
        return self.queue.pull_first()

    def Size(self):                       # Return Size Of The Queue
        return self.queue.Size()
