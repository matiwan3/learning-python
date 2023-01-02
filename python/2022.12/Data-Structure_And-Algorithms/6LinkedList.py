"""
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. Each node in a list consists of at least two parts:

Data
Pointer (Or Reference) to the next node
"""

# Node class
class Node:
    
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    
    # Function to initializ the Linked
    # List object
    def __init__(self):
        self.head = None
        
      
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
        
if __name__ =='__main__':
    
    # Start with empty list
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
'''
Three nodes have been created.
We have references to these three blocks as head,
second and third

llist.head     second             third
    |             |                 |
    |             |                 |
+----+------+     +----+------+     +----+------+
| 1 | None |     | 2 | None |     | 3 | None |
+----+------+     +----+------+     +----+------+
'''
  
llist.head.next = second; # Link first node with second
  
'''
Now next of first Node refers to second. So they
both are linked.

llist.head     second             third
    |             |                 |
    |             |                 |
+----+------+     +----+------+     +----+------+
| 1 | o-------->| 2 | null |     | 3 | null |
+----+------+     +----+------+     +----+------+
'''

second.next = third; # Link second node with the third node

'''
Now next of second Node refers to third. So all three
nodes are linked.

llist.head     second             third
    |             |                 |
    |             |                 |
+----+------+     +----+------+     +----+------+
| 1 | o-------->| 2 | o-------->| 3 | null |
+----+------+     +----+------+     +----+------+
'''
llist.printList()