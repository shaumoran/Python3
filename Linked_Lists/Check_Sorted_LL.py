#Checks if a Linked List is sorted

def issorted(ll):
	ptr = ll.head
	while ptr.next != None:
		if ptr.item > ptr.next.item:
			return False
		ptr = ptr.next
	return True
