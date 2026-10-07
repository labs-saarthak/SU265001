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

# Tree traversal ==> DFS(pre-order,in-order,post-order),BFS(Level order)
def pre_order(root):
    if root:
        print(root.data,end="-->")
        pre_order(root.left)
        pre_order(root.right)
print()
pre_order(root)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data,end="-->")
        in_order(root.right)
print()
in_order(root)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data,end="-->")
print()
post_order(root)

