class Circular_Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.q = [None] * self.size 

    def enqueue(self,val):
        # Queue if full
        if self.front == (self.rear + 1) % self.size:
            return "Queue is full"
        # Queue is empty
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = val 
