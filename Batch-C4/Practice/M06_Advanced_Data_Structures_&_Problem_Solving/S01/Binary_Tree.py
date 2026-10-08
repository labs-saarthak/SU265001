'''
Trees: Trees are non-linear DS
--> The data can be stored in Nodes
Non - Linear : The data can be organized in non sequential order
The data can be arranged in a hierarchical ordrr

Representation : 
           10
          /  \
        20    30
       /  \    \
     40   50    60 

Key Components:
1. Node -> the data to be stored
2. Root -> The Top most node is considered as root
3. Edges -> Connections or links btw the nodes 
4. parent/Child ->   
5. Siblings -> Derived some same parent 
6. Leaf -> Bottom nodes

Applications:
1. File System
2. College Management
3. HTML tags
4. Family Tree

The node part contains of 3 parts:
1. data Part
2. Left Part
3. Right Part

Types: 
1. Binary Tree
2. Binary Search Tree
3. N-ary Tree
4. AVL Tree
5. Red Black Tree

1. Binary Tree: The tree contains of at most of 2 nodes:
Representation : 
           10
          /  \
        20    30
       /  \    \
     40   50    60 

Algorithm of Creating and inserting Data:
1. Create node
2. Insert the data

#Tree Traversal:3 Types

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
4. Traverse through root.right part'''

#In-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root Node
4. Traverse through root.right part'''

#Post-Order:
#Algorithm:
'''
1. Check whether root node is exist or not :
   ---> If not : return Nothing
2. Trvaerse Through root.left part
3. Traverse through root.right part
4. Traverse through root Node'''

class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
def preorder(root):
    if root is None:
        return 
    print(root.data, end = "  ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end =" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right) 
    print(root.data, end =" ")
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