#Counts number of elements in a LL

def count(self):
    count = 0
    ptr = self.head
    while ptr != None:
        count = count + 1
        ptr = ptr + 1
    return count
