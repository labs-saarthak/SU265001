'''
Binary Search Tree: BST is a Binary Tree which follows 2 rules:
1. The value is smallest when comapare with the curr val insert in left sub-tree
2. The value is larger when comapare with the curr val insert in right sub-tree
3. It is applicable for all the nodes not for root node

Representation :
               50
            /    \
          40       70
         /  \     /  \
        20  45    60  80 

Left- sub-tree : 20 , 45 , 40 < root node(50)
Right sub -tree : 60, 70 , 80 > root node(50)
'''
#Creation of BST
class  Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root  = Node(50)
root.left = Node(40)
root.left.left = Node(20)
root.left.right = Node(45)

root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)

'''
Operations:
1. Search
2. Insert 
3. Delete
4. Validation
5. Traversal

Algorithm:
1. check with root node -->return None
2. if key == node.data:
    ---> return True
3. if  key > node.data:
   --->Search in right sub -tree
4. -->Search in left sub-tree

'''
# Search in BST:
class  Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search(root, key):
    if root is None:
        return False
    if key == root.data:
        return True
    if key > root.data:
        return search(root.right, key)   
    return search(root.left, key)

def insert(root,key):
    if root is None:
        return Node(key)
    if key > root.data:
        root.right = insert(root.right,key)
    elif key < root.data:
        root.left = insert(root.left, key)
    return root  

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

root  = Node(50)
root.left = Node(40)
root.left.left = Node(20)
root.left.right = Node(45)

root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)

print(search(root,60))
print(search(root,100))

print("Before Insertion: ")
inorder(root)
root = insert(root, 65)
print("After Insertion: ")
inorder(root)

root = insert(root, 150)
print("After Insertion: ")
inorder(root)


'''
Insertion: Insertion follows the searching rules
Algorithm:
1. if the root is None:
   -->Create a newnode
   --> Return it
2. if key > root.data:
   --->Insert it into right sub-tree
3. if key < root.data:
   --> Insert it into left sub-tree
4. return root

After Inserting to return the values use traversal method(in-order)
'''