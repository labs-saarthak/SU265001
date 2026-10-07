'''
Tree : Trees are non -linear DS
--> Non -linear : the data can be arranged in non-sequential
--> The data can be store in nodes
-->Node contains of 3 parts
   -->1. data part
   -->2. Left part
   -->3. Right part

Representation of Tree:

            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2

Key Components:
1. Node --> Contains the data
2. Root --> Top Node is called as Root node (10)
3. Edges --> Links or connection btw the nodes
4. Parent/child --> One node derived from another(20-Parent node and 40-child node)
5. Siblings --> Two child nodes with a single parent node(20-parent and 40,50 are siblings)
6. Levels --> 
7. Height --> Height of tree 

Applications of Tree:
1. File System
2. HTML Tags
3. School Management

Types of Tree:
1. Binary Tree
2. Binary Search Tree
3. N-ary Tree
4. AVL Tree
5. Red black Tree
'''

#1. Binary Tree:
#A Binary Tree is a Tree which contains of atmost of 2 children
'''
0 children
1 children
2 children

Representation:
            10  --->Level 0
           /  \
          20   30  ---->Level 1
         / \     \
       40  50    60   ---->Level 2
  
'''
#Binary Tree Construction:
'''class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)'''

#Tree Traversal:3 Types
'''
1. Pre-order :  Root --> Left --> Right
2. In-order : Left --> Root --> Right
3. Post-order : Left --> Right --> Root
'''
#Pre-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Traverse through root Node
3. Trvaerse Through root.left part
4. Traverse through root.right part
'''
#In-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root Node
4. Traverse through root.right part
'''
#Post-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root.right part
4. Traverse through root Node
'''
#Leet Code : 94, 144, 145, 226
class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
def preorder(root):
    if root is None:
        return 
    print(root.data, end = " -> ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end = " -> ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data, end = " -> ")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
print("Pre-order Tree Traversal:")
preorder(root)
print()

print("In-order Tree Traversal:")
inorder(root)
print()

print("Post-order Tree Traversal:")
postorder(root)
print()