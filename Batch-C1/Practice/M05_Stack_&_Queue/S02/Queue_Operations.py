# Implementation of a Queue using Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.rear = self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        del_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return del_val

    def peek(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
queue = Queue_LL()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
queue.dequeue()
queue.display()
print(queue.peek())