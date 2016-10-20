#Linked Lists class which contains functions for manipulating Linked Lists

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next   
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        ptr = self.head
        count = 0
        while ptr != None:
            count = count + 1
            ptr = ptr.next
        return count


    def before(self, other):
        ptr = self.head
        before = None
        while ptr.item != None:
            if ptr.item == other:
                return before
            before = ptr.item
            ptr = ptr.next


    def append(self, addend):
        ptr = self.head
        endlessone = Node
        if self.head == None:
            self.add(addend)
        while ptr != None:
            endlessone = ptr
            ptr = ptr.next
        endlessone.next = Node(addend, None)


    def rotate(self):
        self.append(self.head.item)
self.remove()
