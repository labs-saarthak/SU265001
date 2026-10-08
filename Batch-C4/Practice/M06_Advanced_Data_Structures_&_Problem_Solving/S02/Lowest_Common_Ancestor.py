'''
Ancestor : It is a node before node
      10     
     /  \
   20    30   
  /  \    \
40   50    60    

p = 40
q =50 
40: 40 -> 20 -> 10
50 : 50 -> 20 -> 10
Ancestor(40,50) --> 20,10
LCA(40,50) --> 20

Algorithmn:
1. if root is None --> return None
2. if root == either p or q
    -->return root
3. Calculate left & right
4. if left is not none and right is not none:
    ---> curr = LCA
5. if left is none:
   -->return right
6. return left 
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def LCA(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)
    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    else:
        return right
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)

p = root.left.left
q = root.left.right
res = LCA(root,p,q)
print("LCA is: ",res.data)

