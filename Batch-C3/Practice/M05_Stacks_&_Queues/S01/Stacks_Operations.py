'''
Stacks:Stack is a linear DS which follows LIFO
LIFo-->Last in First Out
Operations:
4 
1. Push -->Inserting the elements
2. Pop  --> Remove  the data
3. Peek -->View the last element without removing 
4. is_empty -->Stack is empty or not

Key Points:
1. Overflow -->Trying to insert in already filled stack
2. Underflow -->Trying to remove from the empty stack

Implementation:
2 ways
1) Using List
2) Using Linked List
'''
#Stack using List:
class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items) == 0
    #find the length of stack
    def size(self):
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)
print(s.pop())
print(s.peak())
print(s.is_empty())
print(s.size())

#Stack using Linked List:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if not self.is_empty():
            val = self.top.data
            self.top = self.top.next
            return val
        return "Stack is Empty"
    def peak(self):
        if not self.is_empty():
            return self.top.data
        return "Stack is Empty"
    def is_empty(self):
        return self.top is None
    def traverse(self):
        elements = []
        curr = self.top
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.traverse())
print(s.pop())
print(s.peak())
print(s.is_empty())
        

    

