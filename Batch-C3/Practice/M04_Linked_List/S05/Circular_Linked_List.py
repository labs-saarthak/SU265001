'''
Circular Linked List :
The Last node connects to the first node
Algorithm :
1. Create a node
2. Insert the data
3. Connect the nodes
4. Traverse the nodes

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
def traverse():
    curr = node1
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next 
        if curr == node1:
            break
    print("HEAD")
traverse()
