#Removes every second element in a Linked List

def remove_every_second(ll):
    ptr = ll.head
    while ptr.next != None and ptr != None:
        ptr.next = ptr.next.next
        ptr = ptr.next
