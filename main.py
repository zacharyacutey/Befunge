import readchar

UNIT_TEST_MODE = True

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
  
