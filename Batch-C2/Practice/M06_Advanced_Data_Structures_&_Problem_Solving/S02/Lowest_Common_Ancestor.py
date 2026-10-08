'''
Simple Recursive Approach (Binary Tree)
If current node is None, return None.
If current node is one of the target nodes (p or q), return it.
Search in left subtree.
Search in right subtree.
If both left and right return a node, current node is the LCA.
Otherwise return whichever side found a node.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#Tree structure
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def LCA(root,p,q):
    if root is None:
        return None
    if root.data == p or root.data == q:
        return root.data
    l = LCA(root.left,p,q)
    r = LCA(root.right,p,q)
    if l and r:
        return root.data
    return l if l else r

print(LCA(root,4,5))