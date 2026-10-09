class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# Tree structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Tree Trversal techniques
'''
1. DFS
    1. pre-order(Root - Left - Right)
    2. in-order(Left - Root - Right)
    3. post-order(Left - Right - Root)
2. BFS(level order)
'''

def Pre_Order(root):
    if root:
        print(root.data,end=" -> ")
        Pre_Order(root.left)
        Pre_Order(root.right)
print("\n Pre_Order Traversal")
Pre_Order(root)

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.data,end = " -> ")
        In_Order(root.right)
print("\n In_order Traversal")
In_Order(root)

def Post_Order(root):
    if root:
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.data,end = " -> ")
print("\n Post_order Traversal")
Post_Order(root)

from collections import deque
def Level_Order(root):
    if root is None:
        return
    d = deque([root])
    while d:
        node = d.popleft()
        print(node.data,end= " -> ")
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)
print("\n Level_order Traversal")
Level_Order(root)

