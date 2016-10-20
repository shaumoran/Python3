#Returns item after item we ask for in a LL

def after(self, item):
    ptr = self.head
    while ptr != None:
        if ptr.item == item:
            return ptr.next
        else:
            ptr = ptr.next 
    return None
