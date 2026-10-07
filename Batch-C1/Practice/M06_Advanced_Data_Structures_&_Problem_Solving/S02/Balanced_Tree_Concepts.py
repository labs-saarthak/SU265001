#Balanced Binary Tree – height difference between left and right subtrees of 
# every node is minimal(<=1).
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

def Height(root):
    if root is None:
        return -1
    l = Height(root.left)
    r = Height(root.right)
    return 1 + max(l,r)

def is_Balanced(root):
    if root is None:
        return True
    l = Height(root.left)
    r = Height(root.right)
    if abs(l - r) <= 1:
        return True
    return False

print(is_Balanced(root))
