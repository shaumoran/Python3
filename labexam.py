class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def is_empty(self):
        return self.head == None


#def sumlist(ll):
#	ptr = ll.head
#	addall = 0
#	while ptr != None:
#		addall = addall + ptr.item
#		ptr = ptr.next
#	return addall 



#def countodds(ll):
#	ptr = ll.head
#	count = 0
#	while ptr != None:
#		if ptr.item % 2 != 0:
#			count = count + 1
#		ptr = ptr.next
#	return count 

#def issorted(ll):
#	ptr = ll.head
#	while ptr.next != None:
#		if ptr.item > ptr.next.item:
#			return False
#		ptr = ptr.next
#	return True

def remove_every_second(ll):
    ptr = ll.head
    while ptr.next != None and ptr != None:
        ptr.next = ptr.next.next
        ptr = ptr.next

#def insert_at_end(ll, addend):
 #   ptr = ll.head
  #  elo = Node
   # if ll.head == None:
    #    ll.add(addend)
    #while ll != None:
      #  elo = ptr
       # ptr = ptr.next
    #elo.next = Node(addend, None)

 
 #def remove_every_second(ll):
  #  ptr = ll.head
   # while ptr != None and ptr.next != None:
    #    ptr.next = ptr.next.next
     #   ptr = ptr.next

def detect_loop(self):
    ptr = self.head
    while ptr != None:
        if ptr.next == self.head
            return True
        else:
            ptr = ptr.next
    return False



class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self):
        self.ll.add(item)

    def pop(self):
        return self.ll.remove()


    def is_empty(self):
        return self.ll.head = None



def count(self):
    count = 0
    ptr = self.head
    while ptr != None:
        count = count + 1
        ptr = ptr + 1
    return count


def contains(self, item):
    ptr = self.head
    while ptr != None:
        if ptr.item == item:
            return True
        else:
            ptr = ptr + 1
    return False

def after(self, item):
    ptr = self.head
    while ptr != None:
        if ptr.item == item:
            return ptr.next
        else:
            ptr = ptr.next 
    return None



def before(self, item):
    ptr = self.item
    before = None 
    while ptr != None: 
        if ptr.item == item:
            return before

        ptr = ptr.next
        before = ptr.item

def even_count(self):
    ptr = self.item
    count = 0 
    while ptr != None:
        if ptr.item % 2 == 0:
            count = count + 1
        ptr = ptr.next
    return count 



















