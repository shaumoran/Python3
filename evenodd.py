#If the length of the word is odd, prints the first and last character.
#If even, prints the second half of the word.

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
