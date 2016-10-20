#Checks for something in Linked List 

def contains(self, item):
    ptr = self.head
    while ptr != None:
        if ptr.item == item:
            return True
        else:
            ptr = ptr + 1
    return False
