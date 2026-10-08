'''
Diameter: Longest Path btw the nodes 
current_dia = left + right + 2 (+2--> include the two edges connecting the current node to its child)
Algorithm:
1. Find the height of Tree
2. Check the condition if root is none --> return 0
3. Find the height of Left sub-tree
4. Find the height of Right sub-tree
5. Calculate the current_dia:
    --> curr_dia = (left + right) + 2
6. Find the length of left_dia
7. Find the length of Right_dia
8. Return max(curr_dia, Left_dia, right_dia)
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
def Diameter(root):
    if root is None:
        return 0
    left = height(root.left)
    Right = height(root.right)
    curr_dia = left + Right + 2
    left_dia = Diameter(root.left)
    right_dia = Diameter(root.right)
    return max(curr_dia, left_dia, right_dia)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.left.left = Node(80)
root.left.left.left.left = Node(100)
print("Height of the Tree is :",height(root))
res = Diameter(root)
print("Diameter of tree: ", res)