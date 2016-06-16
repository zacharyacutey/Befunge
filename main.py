import readchar

UNIT_TEST_MODE = True
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
source = [[[" "]*80]]]*25
class Stack:
  def __init__(self):
    self.value = []
  def pop(self):
    if len(self.value) == 0:
      return 0
    else:
      return self.value.pop()
  def push(self,val):
    self.value.append(val)
#Unit test for stack
if UNIT_TEST_MODE:
  f = Stack()
  assert(f.value == [])
  f.push(2)
  assert(f.value == [2])
  f.push(3)
  assert(f.value == [2,3])
  assert(f.pop() == 3)
  assert(f.value == [2])
  assert(f.pop() == 2)
  assert(f.value == [])
  assert(f.pop() == 0)

def readln():
  try:
    return raw_input()
  except:
    return input()

def remove_newline(s):
  return s[:-1]

def fit(s):
  if len(s)>80:
    return list(s[0:80])
  elif len(s)==80:
    return list(s)
  else:
    return list(s) + [" "]*(80 - len(s))

def read_file(name):
  f = open(name,"r")
  i = 0
  while i != 25:
    source[i] = fit(remove_newline(f.readline()))
    i += 1
  f.close()
if UNIT_TEST_MODE:
  read_file("test.txt")
