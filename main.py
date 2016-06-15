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
