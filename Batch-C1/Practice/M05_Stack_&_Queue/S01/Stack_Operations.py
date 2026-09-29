#Stack implementation using Python List
class Stack:
    def __init__(self):
        self.s = []

    def push(self,val):
        self.s.append(val)

    def is_empty(self):
        return len(self.s) == 0
           
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.s.pop()
    
    def size(self):
        return len(self.s)

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[-1]

st = Stack()
print(st.is_empty()) 
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty()) 
print(st.pop())
print(st.size())
print(st.peek())

#Stack implementation using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack_LL:
    def __init__(self):
        self.top = None
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node 
    def is_empty(self):
        return self.top is None 
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        del_val = self.top.data
        self.top = self.top.next
        return del_val
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data 

    def size(self):
        temp = self.top
        count = 0
        while temp:
            count += 1
            temp = temp.next 
        return count 
    
st_ll = Stack_LL()
print(st_ll.is_empty()) 
st_ll.push(10)
st_ll.push(20)
st_ll.push(30)
print(st_ll.is_empty()) 
print(st_ll.pop())
print(st_ll.size())
print(st_ll.peek())