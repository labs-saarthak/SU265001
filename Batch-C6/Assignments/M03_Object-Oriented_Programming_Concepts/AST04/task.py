import math

class Circle:
   def __init__(self, radius):
      pass
   def area(self):
      pass

class Rectangle:
   def __init__(self, length, breadth):
      pass
   def area(self):
      pass

class Triangle:
   def __init__(self, base, height):
      pass
   def area(self):
      pass
   
if __name__ == '__main__':
   shape = input()

   if shape == "Circle":
      radius = float(input())
      obj = Circle(radius)

   elif shape == "Rectangle":
      length = float(input())
      breadth = float(input())
      obj = Rectangle(length, breadth)

   else:
      base = float(input())
      height = float(input())
      obj = Triangle(base, height)

   print("Area: {:.2f}".format(obj.area()))
