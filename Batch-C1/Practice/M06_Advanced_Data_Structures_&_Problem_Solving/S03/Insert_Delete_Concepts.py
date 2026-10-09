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

# In_order Traversal
def In_order(root):
    if root:
        In_order(root.left)
        print(root.data,end="->")
        In_order(root.right)

print()
In_order(root)

def Insert(root,val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = Insert(root.left,val)
    elif val > root.data:
        root.right = Insert(root.right,val)
    return root

node = Insert(root,1)
print("After Insertion: ")
In_order(node)

def delete_node(root, key):
    # Base Case: The tree is empty, or the key doesn't exist
    if root is None:
        return root
    # 1. Search Phase: Traverse the tree to find the node
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    # 2. Deletion Phase: Found the node!
    else:
        # Case 1 & 2: Node with zero or only one child
        if root.left is None:
            return root.right  # Returns the right child (or None if leaf)
        elif root.right is None:
            return root.left   # Returns the left child
        # Case 3: Node with two children
        # Step A: Find the min value node in the right subtree (successor)
        successor = root.right
        while successor.left is not None:
            successor = successor.left  
        # Step B: Copy the successor's value to this node
        root.val = successor.val
        # Step C: Recursively delete the old successor from the right subtree
        root.right = delete_node(root.right, successor.val)
    return root