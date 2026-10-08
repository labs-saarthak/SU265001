'''
Height : The longest path between the nodes
2 ways
1. Edges
2. Nodes
Representation:
            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2
Height Formula:
Height(Node) = 1 + max(height(left),height(right)) 
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
    Lh = height(root.left)
    Rh = height(root.right)
    if abs(Lh - Rh) > 1:
        return False
    return True'''

def check_height(root):
    if root is None:
        return 0
    Left_height = check_height(root.left)
    if Left_height == -1:
        return -1
    Right_height = check_height(root.right)
    if Right_height == -1:
        return -1
    return 1 + max(Left_height,Right_height)
def is_balanced2(root):
    return check_height != -1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
print("Height of the Tree is :",check_height(root))
if is_balanced2(root):
    print("Given Tree is Balanced")
else:
    print("Not Balanced")

'''
Balancecd Tree: The absolute difference btw height of left and height right <= 1
--> Every Binary Tree is a Balanced Tree
Algortihm: 
1. Find the length of Left sub-tree
2. Find the length of Right sub-tree
3. Calculate the |height(left) - height(right)| <= 1
4. Given Tree is balanced

'''
#Leet Code :110
