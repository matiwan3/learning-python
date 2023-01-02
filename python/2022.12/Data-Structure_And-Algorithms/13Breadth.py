"""
Level order traversal of a tree is breadth-first traversal for the tree. The level order traversal of the above tree is 1 2 3 4 5.

For each node, first, the node is visited and then its child nodes are put in a FIFO queue. Below is the algorithm for the same –

Create an empty queue q
temp_node = root /*start from root*/
Loop while temp_node is not NULL
print temp_node->data.
Enqueue temp_node’s children (first left then right children) to q
Dequeue a node from q
"""


class Node:
    
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        

def printLevelOrder(root):
    
    if root is None:
        return
    
    queue = []
    
    queue.append(root)
    while(len(queue) > 0):
        
        print(queue[0].data)
        node = queue.pop(0)
        
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
            
        if node.right is not None:
            queue.append(node.right)
            
# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)


# Algorithms can be found here: https://www.geeksforgeeks.org/python-data-structures-and-algorithms/