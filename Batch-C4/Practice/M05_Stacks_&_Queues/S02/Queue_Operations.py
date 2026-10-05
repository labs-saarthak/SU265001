''''
Queue: 
It is a linear DS which follows FIFO mechanism
FIFO-->First In First Out
Operations:
4 
1. Enqueue--> Insert data 
2. Dequeue-->Removing of the data
3. Peak-->return the front element
4. is_empty--> to check queue is empty or not(Boolean value)

Important Points : 
1. front --> start
2. rear --> end

Implementation : 2 ways
1. Using List
2. Using Linked List
'''
#1. Using List:
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is Empty"
    def peak(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is Empty"
    def is_empty(self):
        return self.items is None
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.items)
print(q.dequeue())
print(q.peak())
print(q.is_empty())

#Using Linked List:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val
    
    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        res = []
        curr = self.front
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
print("Queue Using Linked List")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.display())
print(q.dequeue())
print(q.is_empty())


