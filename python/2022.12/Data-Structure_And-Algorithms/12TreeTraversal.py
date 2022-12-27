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

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
# A function to do inorder tree traversal
def printInorder(root):
    
    if root:
        
        # First recur on left child
        printInorder(root.left)
        
        # then print the data of node
        print(root.val),
        
        # now recur on right child
        printInorder(root.right)
        
# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        
        # First recur on left child
        printPostorder(root.left)
        
        # the recur on right child
        printPostorder(root.right)
        
        # now print the data of node
        print(root.val),
        
# A function to do preorder tree traversal
def printPreorder(root):
    
    if root:
        
        # First print the data of node
        print(root.val),
        
        # Then recur on left child
        printPreorder(root.left)
        
        # Finally recur on right child
        printPreorder(root.right)
        
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)
