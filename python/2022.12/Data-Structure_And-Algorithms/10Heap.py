"""
heapq module in Python provides the heap data structure that is mainly used to represent a priority queue. The property of this data structure is that it always gives the smallest element (min heap) whenever the element is popped. Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time. It supports the extraction and insertion of the smallest element in the O(log n) times.

Generally, Heaps can be of two types:

Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
"""

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5,7,9,1,3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ",end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ",end="")
print(heapq.heappop(li))