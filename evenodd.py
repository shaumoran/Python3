import sys 
if len(sys.argv[1]) % 2 == 0:
	a = len(sys.argv[1])
	b = a//2 
	print (sys.argv[1][-b:])

else:
	a = sys.argv[1]
	b = a[0]
	c = a[-1:]
	print(b + c)
