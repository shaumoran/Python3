#Sums all the numbers in a Linked List 

def sumlist(ll):
	ptr = ll.head
	addall = 0
	while ptr != None:
		addall = addall + ptr.item
		ptr = ptr.next
	return addall
