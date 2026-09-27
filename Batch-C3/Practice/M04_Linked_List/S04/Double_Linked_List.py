''''
Double Linked List:

'''
#Insertion after a node:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_begin(head, data):
    new_node =Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insert_after_pos(node, data):
    if node is None:
        print("Error")
        return
    new_node = Node(data)
    new_node.next = node.next
    new_node.prev = node
    if node.next:
        node.next.prev = new_node
    node.next = new_node

def insert_before_pos( node, data):
    if node is None:
        print("Error")
        return
    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node
    if node.prev:
        node.prev.next = new_node
    else:
        head = new_node
    node.prev = new_node
    return head

def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head,10)
head = insert_begin(head,20)
head = insert_begin(head,30)

print("Insertion at begin")
traverse(head)
print()

print("after Node")
insert_after_pos(head, 100)
traverse(head)

print("Before Node")
insert_before_pos(head, 500)
traverse(head)