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
def height(root):
    if root is None:
        return -1
    Left_height = height(root.left)
    Right_height = height(root.right)
    return 1 + max(Left_height, Right_height)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)
print("Height of tree is:",height(root))

#Leet Code : 94, 144, 145(Binary tree traversal)