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

def Diameter(root):
    if root is None:
        return 0
    l = Height(root.left)
    r = Height(root.right)
    d = l + r + 2
    d_l = Diameter(root.left)
    d_r = Diameter(root.right)
    return max(d,d_l,d_r)

print(Diameter(root))