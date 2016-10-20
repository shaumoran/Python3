#Returns the number of odd numbers in a Linked List 

def countodds(ll):
	ptr = ll.head
	count = 0
	while ptr != None:
		if ptr.item % 2 != 0:
			count = count + 1
		ptr = ptr.next
	return count 
