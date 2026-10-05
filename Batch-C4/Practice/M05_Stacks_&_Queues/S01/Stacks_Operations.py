'''
Stacks:Stack is a linear DS which follows LIFO
LIFo-->Last in First Out
Operations:
4 
1. Push -->Inserting the elements
2. Pop  --> Remove  the data
3. Peek -->View the last element without removing 
4. is_empty -->Stack is empty or not

# Key Points:
1. Overflow -->
2. Under flow -->

Implementation :
2 ways
1. Using List
2. Using Linked list
'''
#Stack Implementation Using List :
class Stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items) == 0
s =Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.items)
print(s.pop())
print(s.peek())
print(s.is_empty())

#Stack Implementation Using Linked List:
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
            val =self.top.data
            self.top = self.top.next
            return val
        return "Stack is Empty"
    def peek(self):
        if not self.is_empty():
            return self.top.data
        return "Stack is Empty"
    def is_empty(self):
        return self.top is None
    def display(self):
        res = []
        curr = self.top
        while curr:
            res.append(curr.data)
            curr =curr.next
        return res
print("Stack Using Linked List")
s =Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.display())
print(s.pop())
print(s.peek())
print(s.is_empty())
