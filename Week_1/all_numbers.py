#This prints a tuple of even and odd numbers

def get_evenodd_list():
	a = int(input())
	odds = []
	evens = []
	while a != -1:
		if a % 2 != 0:
			odds.append(a)
		else:
			evens.append(a)
		a = int(input())
	return (odds,evens)
