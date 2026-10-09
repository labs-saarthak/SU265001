'''
Deletion in BST: 3 ways
1. Delete the leaf node
2. Delete the 1 child 
3. Delete the 2 children

1. Deletion of Leaf : 
Ex: 
              50
            /   \
          40      70
         /  \    /  \
        20  45  60  80

Delete(20)
Delete(45)
Delete(60)
Delete(80)

2. Deletion of One Child :
Ex: 
              50                            
            /   \
          40      70        
         /  \    /  
        20  45  60  

  Delete(70) --> 1 child = 60
  --> Delete 70 and connect 60 directly to root node(50)
  Output:
              50
             /   \
           40     60     
          /  \     
         20  45  

3. Deletion of Two Child :
Ex: 
              50
             /   \
           40      70
          /  \    /  \
         20  45  60  80

Want  to Delete(70) --> 2 child = (60, 80)
1. We have to find the in-order successor
2. Successor is nothing but, the next smallest element of next delete element
Ex: successor(70) = 80
Explanation: In-order Successor(Left -> Root -> Right) : 20 -> 40 -> 45 -> 50 -> 60 -> 70 -> 80
so, the next smallest elem of 70 is 80
--> Store the val 80
--> Replace 70 with 80
--> Delete the original 80 

Algorithm:
1. check with root node is none --> return none
2. if key < root.data:
    --> delete from Left sub-tree
3. if key > root.data:
   --> Delete from Right sub-tree
4. else:
   --> deletion of leaf 
   --> deletion of 1 child
   --> deletion 2 child
5. return root
'''