#Task
class Student:
   def __init__(self, name, roll_no, marks):
      pass

   def display(self):
      pass
   
if __name__ == '__main__':
   name = input()
   roll_no = int(input())
   marks = int(input())

   student = Student(name, roll_no, marks)
   student.display()
