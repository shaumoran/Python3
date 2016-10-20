#Detects a loop in a Linked List 

def detect_loop(self):
    ptr = self.head
    while ptr != None:
        if ptr.next == self.head
            return True
        else:
            ptr = ptr.next
    return False
