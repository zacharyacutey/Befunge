stack = []
def PushZero():
  stack.append(0)
def PushOne():
  stack.append(1)
def PushTwo():
  stack.append(2)
def PushThree():
  stack.append(3)
def PushFour():
  stack.append(4)
def PushFive():
  stack.append(5)
def PushSix():
  stack.append(6)
def PushSeven():
  stack.append(7)
def PushEight():
  stack.append(8)
def PushNine():
  stack.append(9)
def Add():
  v=stack.pop()
  u=stack.pop()
  stack.append(u+v)
def Subtract():
  v=stack.pop()
  u=stack.pop()
  stack.append(u-v)
def Multiply():
  v=stack.pop()
  u=stack.pop()
  stack.append(u*v)
def Divide():
  v=stack.pop()
  u=stack.pop()
  while v == 0:
    v = AskInteger()
  stack.append(int(u/v))
def Modulo():
  v=stack.pop()
  u=stack.pop()
  while v == 0:
    v = AskInteger()
  stack.append(u%v)
def Not():
  u=stack.pop()
  stack.append(int(not u))
