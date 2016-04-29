LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
pos = [0,0]
vel = RIGHT
stack = []
program = [[' ' j for j in range(25)] for i in range(80)]
def MoveDefault():
  if vel == LEFT:
    pos[0]=(pos[0]-1) % 80
  elif vel == RIGHT:
    pos[0]=(pos[0]+1) % 80
  elif vel == UP:
    pos[1]=(pos[1]-1) % 25
  elif vel == DOWN:
    pos[1]=(pos[1]-1) % 25
def PushZero():
  stack.append(0)
  MoveDefault()
def PushOne():
  stack.append(1)
  MoveDefault()
def PushTwo():
  stack.append(2)
  MoveDefault()
def PushThree():
  stack.append(3)
  MoveDefault()
def PushFour():
  stack.append(4)
  MoveDefault()
def PushFive():
  stack.append(5)
  MoveDefault()
def PushSix():
  stack.append(6)
  MoveDefault()
def PushSeven():
  stack.append(7)
  MoveDefault()
def PushEight():
  stack.append(8)
  MoveDefault()
def PushNine():
  stack.append(9)
  MoveDefault()
def Add():
  v=stack.pop()
  u=stack.pop()
  stack.append(u+v)
  MoveDefault()
def Subtract():
  v=stack.pop()
  u=stack.pop()
  stack.append(u-v)
  MoveDefault()
def Multiply():
  v=stack.pop()
  u=stack.pop()
  stack.append(u*v)
  MoveDefault()
def Divide():
  v=stack.pop()
  u=stack.pop()
  while v == 0:
    v = AskInteger()
  stack.append(int(u/v))
  MoveDefault()
def Modulo():
  v=stack.pop()
  u=stack.pop()
  while v == 0:
    v = AskInteger()
  stack.append(u%v)
  MoveDefault()
def Not():
  u=stack.pop()
  stack.append(int(not u))
  MoveDefault()
def Greater():
  v=stack.pop()
  u=stack.pop()
  stack.append(u>v)
  MoveDefault()
def Right():
  global vel
  vel=RIGHT
  MoveDefault()
def Left():
  global vel
  vel = RIGHT
  MoveDefault()
def Up():
  global vel
  vel = UP
  MoveDefault()
def Down():
  global vel
  vel = DOWN
  MoveDefault()
def RandomDirection():
  global vel
  import random
  u=random.choice([UP,DOWN,LEFT,RIGHT])
  vel=u
  MoveDefault()
