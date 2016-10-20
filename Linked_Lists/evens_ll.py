#Returns even numbers in a LL

def even_count(self):
    ptr = self.item
    count = 0 
    while ptr != None:
        if ptr.item % 2 == 0:
            count = count + 1
        ptr = ptr.next
    return count 
