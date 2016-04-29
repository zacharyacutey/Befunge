LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
pos = [0,0]
vel = RIGHT
stack = []
program = [[j for j in range(25)] for i in range(80)] #Temporary value
is_string = False

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
def HorizontalIf():
  global vel
  u=stack.pop()
  if u == 0:
    vel = RIGHT
  else:
    vel = LEFT
  MoveDefault()
def VerticalIf():
  global vel
  u=stack.pop()
  if u == 0:
    vel = DOWN
  else:
    vel = UP
  MoveDefault()
def StringMode():
  global is_string
  is_string = not is_string
  MoveDefault()
def Duplicate():
  u=stack.pop()
  stack.append(u)
  stack.append(u)
def Swap():
  u=stack.pop()
  v=stack.pop()
  stack.append(u)
  stack.append(v)
def Pop():
  stack.pop()
def PutInteger():
  print(stack.pop())
def PutASCII():
  print(chr(stack.pop()))
def Bridge():
  MoveDefault()
  MoveDefault()
def Get():
  y=stack.pop()
  x=stack.pop()
  if 0 <= y < 25:
    stack.append(0)
    MoveDefault()
    return
  if 0 <= x < 80:
    stack.append(0)
    MoveDefault()
    return
  stack.append(ord(program[x][y]))
  MoveDefault()
def Put():
  y=stack.pop()
  x=stack.pop()
  v=stack.pop()
  program[x][y]=ord(v)
  MoveDefault()
def AskInteger():
  try:
    i=raw_input
  except NameError:
    i=input
  f = i()
  stack.append(int(f))
  MoveDefault()
def AskASCII():
  import readchar
  c=readchar.readchar()
  stack.append(ord(c))
  MoveDefault()
def Terminate():
  exit()
def ExtendLine(line):
  if len(line)==80:
    return line
  if len(line)<80:
    return ExtendLine(line+' ')
  if len(line)>80:
    return line[0:80]
def EvalSquare():
  global vel
  t=program[pos[0]][pos[1]]
  if not is_string:
    if t=='+':
      Add()
    elif t=='-':
      Subtract()
    elif t=='*':
      Multiply()
    elif t=='/':
      Divide()
    elif t=='%':
      Modulo()
    elif t=='!':
      Not()
    elif t=='`':
      return Greater()
    elif t=='>':
      Right()
    elif t=='<':
      Left()
    elif t=='v':
      Down()
    elif t=='^':
      Up()
    elif t=='?':
      RandomDirection()
    elif t=='|':
      VerticalIf()
    elif t=='_':
      HorizonatlIf()
    elif t=='"':
      StringMode()
    elif t==':':
      Duplicate()
    elif t=='$':
      Pop()
    elif t=='\\':
      Swap()
    elif t=='.':
      PutInteger()
    elif t==',':
      PutAscii()
    elif t=='#':
      Bridge()
    elif t=='g':
      Get()
    elif t=='p':
      Put()
    elif t=='~':
      GetASCII()
    elif t=='&':
      GetInteger()
    elif t=='@':
      Terminate()
    elif t=='0':
      PushZero()
    elif t=='1':
      PushOne()
    elif t=='2':
      PushTwo()
    elif t=='3':
      PushThree()
    elif t=='4':
      PushFour()
    elif t=='5':
      PushFive()
    elif t=='6':
      PushSix()
    elif t=='7':
      PushSeven()
    elif t=='8':
      PushEight()
    elif t=='9':
      PushNine()
    else:
      MoveDefault()
def EvaluateFile(name):
  global program,vel
  f=open(name)
  temp=[]
  for i in range(25):
    u=f.readline()
    temp.append(list(ExtendLine(u[:len(u)-1])))
  program=[[temp[j][i] for j in range(25)] for i in range(80)]
EvaluateFile("wumpus.txt")
while True:
  EvalSquare()
