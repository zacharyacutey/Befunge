#Starting over, but in python, must install readchar for this to work!!!
import readchar

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

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
