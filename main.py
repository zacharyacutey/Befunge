stack = []
def Add():
  u=stack.pop()
  v=stack.pop()
  stack.append(u+v)
def Subtract():
  u=stack.pop()
  v=stack.pop()
  stack.append(v-u)
