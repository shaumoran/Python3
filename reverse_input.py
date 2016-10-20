import Stack 
stack = Stack()
for v in "aeoiu":
   stack.push(v)
while not stack.isempty():
   print(stack.pop())