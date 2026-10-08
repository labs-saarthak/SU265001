class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# BST structure
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.right = Node(7)
root.right.left = Node(15)

# Search in BST
def Search(root,val):
    if root is None:
        return False
    if root.data == val:
        return True
    elif val < root.data:
        return Search(root.left,val)
    else:
        return Search(root.right,val)
    return False

print(Search(root,5))
print(Search(root,30))