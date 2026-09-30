''''
Queues: Queues is a linear DS which follows FIFO
FIFO--> First In First Out

Operations : 
4
1. Enqueue -->Insert the data
2. Dequeue --> removing the element
3. Peak --> returns the starting of the node without removing
4. is_empty -->Checks the queue is empty or not (Boolean Output)

Key words:
1. front --> starting of the queue
2. rear --> Ending of the queue

Implementation:
2
1. Using List
2. Using Linked List
'''

#Queues using List:
class Queues:
    def __init__(self):
        self.items = []
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Stack is Empty"
    def peak(self):
        if not self.is_empty():
            return self.items[0]
        return "Stack is Empty"
    def is_empty(self):
        return len(self.items) == 0
    #find the length of stack
    def size(self):
        return len(self.items)

s = Queues()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
print(s.items)
print(s.dequeue())
print(s.peak())
print(s.is_empty())
print(s.size())

#USing Linked List:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        pass

    def dequeue(self):
        pass

    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        res = []
        curr = self.front
        while curr:
            res.append(curr.data)
            curr = curr.next 
        return res

#Leet Code - 232:

