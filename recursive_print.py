def rprint(a,b):
	if a == b:
		return 
	else:
		print(a) 
		rprint(a+1,b)
