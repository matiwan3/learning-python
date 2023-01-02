"""
Binary Search Tree is a node-based binary tree data structure that has the following properties:

The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
Binary Searcch Tree

The above properties of the Binary Search Tree provide an ordering among keys so that the operations like search, minimum and maximum can be done fast. If there is no order, then we may have to compare every key to search for a given key.

Searching Element
Start from the root.
Compare the searching element with root, if less than root, then recurse for left, else recurse for right.
If the element to search is found anywhere, return true, else return false.
"""

# A utlitity function to search a given key in BST
def search(root, key):
    
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    
    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left,key)