'''
Diameter : Longest Path btw the nodes
Formula:
curr_dia = (left + right) + 2
Algorithm :
1. Find the Length of left sub-tree
2. Find the Length of Right sub-tree
3. Calculate the current Diameter
4. Find the length of left dia
5. Find the length of right dia
6. Return maximum(curr_dia, left_dia, right_dia)

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
def diameter(root):
    if root is None:
        return -1
    left = height(root.left)
    right = height(root.right)
    curr_dia = left + right + 2
    left_dia = diameter(root.left)
    right_dia = diameter(root.right)
    return max(curr_dia, left_dia, right_dia)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
root.right.right = Node(60)
res = diameter(root)
print("Diameter is: ",res)

#Leet Code : 543