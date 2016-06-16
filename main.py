import readchar

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

direction = RIGHT
string_mode = False
position = [0,0]
source = [[" " for j in range(80)] for i in range(25)]
def delta(direct):
  if direct == RIGHT:
    return [1,0]
  elif direct == LEFT:
    return [-1,0]
  elif direct == UP:
    return [0,1]
  elif direct == DOWN:
    return [0,-1]
  else:
    raise "WTF, GO AND FIX THIS!"
def get_input():
  try:
    return raw_input()
  except:
    return input()

def get_chr(i):
  try:
    return unichr(i)
  except:
    return chr(i)
class Stack:
  def __init__(self):
    self.value = []
  def pop(self):
    if len(self.value) == 0:
      return 0
    return self.value.pop()
  def push(self,value):
    self.value.append(value)

class Program(Stack):
  def PushZero(self): self.push(0)
  def PushOne(self): self.push(1)
  def PushTwo(self): self.push(2)
  def PushThree(self): self.push(3)
  def PushFour(self): self.push(4)
  def PushFive(self): self.push(5)
  def PushSix(self): self.push(6)
  def PushSeven(self): self.push(7)
  def PushEight(self): self.push(8)
  def PushNine(self): self.push(9)
  def Add(self):
    a = self.pop()
    b = self.pop()
    self.push(b+a)
  def Subtract(self):
    a = self.pop()
    b = self.pop()
    self.push(b-a)
  def Multiply(self):
    a = self.pop()
    b = self.pop()
    self.push(b*a)
  def Divide(self):
    a = self.pop()
    b = self.pop()
    while a == 0:
      a = int(get_input())
    self.push(int(b/a))
  def Modulo(self):
    a = self.pop()
    b = self.pop()
    while a == 0:
      a = int(get_input())
    self.push(b%a)
  def Not(self):
    a = self.pop()
    if a == 0:
      self.push(1)
    else:
      self.push(0)
  def Greater(self):
    a = self.pop()
    b = self.pop()
    if b > a:
      self.push(1)
    else:
      self.push(0)
  def MoveLeft(self):
    global direction
    direction = LEFT
  def MoveRight(self):
    global direction
    direction = RIGHT
  def MoveUp(self):
    global direction
    direction = UP
  def MoveDown(self):
    global direction
    direction = DOWN
  def MoveRandom(self):
    global direction
    import random
    direction = random.choice([LEFT,RIGHT,UP,DOWN])
  def HorizontalIf(self):
    a = self.pop()
    if a == 0:
      self.MoveRight()
    else:
      self.MoveLeft()
  def VerticalIf(self):
    a = self.pop()
    if a == 0:
      self.MoveDown()
    else:
      self.MoveUp()
  def StringMode(self):
    global string_mode
    string_mode = 2
  def Duplicate(self):
    a = self.pop()
    self.push(a)
    self.push(a)
  def Swap(self):
    a = self.pop()
    b = self.pop()
    self.push(a)
    self.push(b)
  def Pop(self):
    self.pop()
  def OutInt(self):
    import sys
    a = self.pop()
    sys.stdout.write(a)
  def OutAscii(self):
    import sys
    a = self.pop()
    sys.stdout.write(get_chr(a))
  def Bridge(self):
    global position
    x = (position[0]+delta(direction)[0])
    x %= 80
    y = (position[1]+delta(direction)[0])
    y %= 25
    position = [x,y]
  def Get(self):
    y = self.pop()
    x = self.pop()
    if not ((0 <= x < 80) and (0 <= y < 25)):
      self.push(0)
    else:
      self.push(ord(source[x][y]))
  def Put(self):
    y = self.pop()
    x = self.pop()
    v = self.pop()
    if not ((0 <= x < 80) and (0 <= y < 25)):
      raise "FIX THIS YOU IDIOT!"
    source[x][y] = get_chr(v)
  def AskInt(self):
    s = int(get_input())
    self.push(s)
  def AskAscii(self):
    s = readchar.readchar()
    self.push(ord(s))
  def Terminate(self):
    import sys
    sys.exit()

bf = Program()
def make_fit(s):
  if len(s) > 80:
    return list(s[0:80])
  elif len(s) < 80:
    return make_fit(s+" ")
  else:
    return make_fit(s)
def remove_newline(s):
  return s[:-1]
def read_file(name):
  global source
  s = []
  f = open(name,"r")
  for dummy_i in range(25):
    try:
      s.append(make_fit(remove_newline(f.readline())))
    except:
      s.append([" "]*80)
  f.close()
  source = s

def current_char():
  return source[position[0]][position[1]]

def move():
  position[0]+=delta(direction)[0] % 80
  position[1]+=delta(direction)[1] % 25

def step():
  global string_mode
  if not string_mode:
    if current_char()=="0":
      bf.PushZero()
    elif current_char()=="1":
      bf.PushOne()
    elif current_char()=="2":
      bf.PushTwo()
    elif current_char()=="3":
      bf.PushThree()
    elif current_char()=="4":
      bf.PushFour()
    elif current_char()=="5":
      bf.PushFive()
    elif current_char()=="6":
      bf.PushSix()
    elif current_char()=="7":
      bf.PushSeven()
    elif current_char()=="8":
      bf.PushEight()
    elif current_char()=="9":
      bf.PushNine()
    elif current_char()=="+":
      bf.Add()
    elif current_char()=="-":
      bf.Minus()
    elif current_char()=="*":
      bf.Multiply()
    elif current_char()=="/":
      bf.Divide()
    elif current_char()=="%":
      bf.Modulo()
    elif current_char()=="!":
      bf.Not()
    elif current_char()=="`":
      bf.Greater()
    elif current_char()==">":
      bf.MoveRight()
    elif current_char()=="<":
      bf.MoveLeft()
    elif current_char()=="v":
      bf.MoveDown()
    elif current_char()=="^":
      bf.MoveUp()
    elif current_char()=="?":
      bf.Random()
    elif current_char()=="_":
      bf.HorizontalIf()
    elif current_char()=="|":
      bf.VerticalIf()
    elif current_char()=='"':
      string_mode=True
    elif current_char()==":":
      bf.Duplicate()
    elif current_char()=="\\":
      bf.Swap()
    elif current_char()=="$":
      bf.Pop()
    elif current_char()==".":
      bf.OutInt()
    elif current_char()==",":
      bf.OutAscii()
    elif current_char()=="#":
      bf.Bridge()
    elif current_char()=="g":
      bf.Get()
    elif current_char()=="p":
      bf.Put()
    elif current_char()=="@":
      bf.Terminate()
    elif current_char()=="&":
      bf.AskInt()
    elif current_char()=="~":
      bf.AskAscii()
    else:
      1 + 1 == 2
  else:
    if current_char()=='"':
      string_mode = False
    bf.push(ord(current_char()))
  bf.Bridge()
def main_loop(program_name):
  global source
  read_file(program_name)
  while True:
    step()
#main_loop("test.txt")
