'''
Ancestor : It is also a node that comes before a node
Representation:
            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2

p =40
q =50
path(40): 40 -> 20 -> 10 
path(50): 50 -> 20 -> 10
LCA(40,50) : 20 & 10

Algorithm:
1. Check with root 
2. if root either equal to p or q
   --> return root
3. Find the Left -sub tree
4. Search through Left Sub tree
5. Search through Right Sub tree
6. If both sides exists same node:
   --> that is the LCA
7. If only on side is exists:
   -->return that node
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def LCA(root,p,q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    return right
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

p = root.left.left  #40
q = root.left.right  #50
res = LCA(root,p,q)
print("Lowest Common Ancestor:",res.data)

