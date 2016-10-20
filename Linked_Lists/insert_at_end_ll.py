#Inserts an element to the end of a Linked List 
def insert_at_end(ll, addend):
   ptr = ll.head
   elo = Node
   if ll.head == None:
      ll.add(addend)
   while ll != None:
      elo = ptr
      ptr = ptr.next
   elo.next = Node(addend, None)
