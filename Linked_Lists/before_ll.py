#Returns item before item we ask for in a LL

def before(self, item):
    ptr = self.item
    before = None 
    while ptr != None: 
        if ptr.item == item:
            return before

        ptr = ptr.next
        before = ptr.item
