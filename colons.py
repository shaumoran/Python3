import sys 
word = sys.argv[1:]
bs = " "
for a in word:
	bs = bs + ":" + a

bs = bs + ":"
print(bs)
