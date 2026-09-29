'''
Double Linked List : 
The data can be store in the nodes
Nodes --> 3 parts
1.data
2.Prev
3.Next
Algorithm:
1. Create node
2. insert data
3. connection
4. traverse

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

def traverse_forward():
    curr = node1
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next 
    print("None")
#Write the code to print in reverse order?
def traverse_backward():
    curr = node4
    while curr:
            print(curr.data, end = " <-> ")
            curr = curr.prev
    print("None")
traverse_forward()
traverse_backward()
'''

#Insertion of a node at the beginning:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next 
    curr.next = new_node
    new_node.prev = curr.next
    return head
def insert_after_node(node, data):
    if node is None:
        print("Error")
        return
    





def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head , 50)
head = insert_begin(head , 60)
head = insert_begin(head , 70)
print("Insertion at the Begin")
traverse(head)
print()

print("Insertion at the end")
head = insert_end(head, 100)
traverse(head)

