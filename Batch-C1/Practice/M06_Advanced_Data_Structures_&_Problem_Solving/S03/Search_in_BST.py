class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# BST structure
root = Node(10)
root.left = Node(7)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(9)
root.right.left = Node(15)

def Search(root,key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return Search(root.left,key)
    else:
        return Search(root.right,key)

print(Search(root,5)) 
print(Search(root,35)) 