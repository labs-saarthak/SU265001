''''
Circular Queue:
The rear position is connected to Front position
Usage:
--> To Re-use the empty spaces after performing dequeue operation
Operations: 4
1. Enqueue
2. Dequeue
3. is_empty
4. is_full
'''
class CircularQueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def enqueue(self,data):
        if  self.is_full():
            return "Queue is full"
        self.rear = (self.rear + 1)% self.capacity
        self.queue[self.rear] = data
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        val = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val
    def display(self):
        if self.is_empty():
            return "Queue is Empty"
        res = []
        for i in range(self.size):
            index = (self.front + i ) % self.capacity
            res.append(self.queue[index])
        return res
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print(cq.display())
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(60)
cq.enqueue(70)
print(cq.display())