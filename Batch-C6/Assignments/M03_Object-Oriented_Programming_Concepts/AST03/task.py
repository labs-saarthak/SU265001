#Tasks
class Person:
    def __init__(self, name, age):
        pass

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        pass

    def display(self):
        pass

if __name__ == '__main__':
    name = input()
    age = int(input())
    roll_no = int(input())
    course = input()

    student = Student(name, age, roll_no, course)
    student.display()


