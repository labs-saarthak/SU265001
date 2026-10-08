'''
Height Tree: Longest path that can be traverse through root to leaf
2 Conventions:
1. Edges
2. Nodes

              10    --> Node1
Edge1<--     /  \
           20    30   ---->Node2
Edge2<--  /  \    \
        40   50    60    -->Node3

Based upon Edges --> height : 2
Based upon Nodes --> height : 3

Formual: 
Height(Node) = 1 + max(height(left),height(right))

Algorithm:
1. check the condition whether root is exist:
   --> return -1
2. Find the length of the left sub-tree
3. Find the length of the right sub-tree
4. Return 1 + max(left,right)

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
'''def height(root):
    if root is None:
        return -1
    Left_height = height(root.left)
    Right_height = height(root.right)
    return 1 + max(Left_height, Right_height)

def is_balanced(root):
    if root is None:
        return True
    left = height(root.left)
    right = height(root.right)
    if abs(left - right) >1:
        return False
    return True
'''
def check_height(root):
    if root is None:
        return 0
    Lh = check_height(root.left)
    if Lh == -1:
        return -1
    Rh = check_height(root.right)
    if Rh == -1:
        return -1
    return 1 + max(Lh,Rh)
def is_balanced(root):
    return check_height != -1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)
print("Height of tree is:",check_height(root))
print()
if is_balanced(root):
    print("Given Tree is Balanced")
else:
    print("Given Tree is not Balanced")

#Leet Code : 94, 144, 145(Binary tree traversal)

'''
Balanced Tree: The absolute  difference btw the height of left sub-tree and heoight of right sub tree
should always <= 1
-->Every Binary Tree is a Balanced Tree
ALgorithm :
1. Check with root
2. Find the length of left sub-tree
3. Find the length of right sub-tree
4. if abs(left - right) > 1:
    --> return False
5. return True
'''
#Leet Code : 110