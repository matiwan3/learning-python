"""
A tree is a gierarchical data structure that looks like the below figure: <img>

The topmost node of the tree is called the root whereas the bottommost nodes or the nodes with no children are called the leaf nodes. The nodes that are directly under a node are called its children and the nodes that are directly above something are called its parent.

A binary tree is a tree whose elements can have almost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. A Binary Tree node contains the following parts.

Data
Pointer to left child
Pointer to the right child
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)


