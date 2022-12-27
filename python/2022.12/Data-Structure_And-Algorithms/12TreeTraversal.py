"""
    Trees can be traversed in different ways. Following are the generally used ways for traversing trees. Let us consider the below tree –

     tree
    ----
     1    <-- root
   /   \
  2     3  
 / \
4   5
Depth First Traversals:

Inorder (Left, Root, Right) : 4 2 5 1 3
Preorder (Root, Left, Right) : 1 2 4 5 3
Postorder (Left, Right, Root) : 4 5 2 3 1
Algorithm Inorder(tree)

Traverse the left subtree, i.e., call Inorder(left-subtree)
Visit the root.
Traverse the right subtree, i.e., call Inorder(right-subtree)
Algorithm Preorder(tree)

Visit the root.
Traverse the left subtree, i.e., call Preorder(left-subtree)
Traverse the right subtree, i.e., call Preorder(right-subtree)
Algorithm Postorder(tree)

Traverse the left subtree, i.e., call Postorder(left-subtree)
Traverse the right subtree, i.e., call Postorder(right-subtree)
Visit the root.
"""
