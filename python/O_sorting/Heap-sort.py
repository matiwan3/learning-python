# Heapsort is an efficient sorting algorithm based on the use of max/min heaps. A heap is a tree-based data structure that satisfies the heap property – that is for a max heap, the key of any node is less than or equal to the key of its parent (if it has a parent).

# This property can be leveraged to access the maximum element in the heap in O(logn) time using the maxHeapify method. We perform this operation n times, each time moving the maximum element in the heap to the top of the heap and extracting it from the heap and into a sorted array. Thus, after n iterations we will have a sorted version of the input array.

# The algorithm is not an in-place algorithm and would require a heap data structure to be constructed first. The algorithm is also unstable, which means when comparing objects with same key, the original ordering would not be preserved.

# This algorithm runs in O(nlogn) time and O(1) additional space [O(n) including the space required to store the input data] since all operations are performed entirely in-place.

# The best, worst and average case time complexity of Heapsort is O(nlogn). Although heapsort has a better worse-case complexity than quicksort, a well-implemented quicksort runs faster in practice. This is a comparison-based algorithm so it can be used for non-numerical data sets insofar as some relation (heap property) can be defined over the elements.

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2
    
# See if left child of root exists and is greater than root

    if l < n and arr[i] < arr[l]:
        largest = l
# See if right child of root exists and is grater than root

    if r < n and arr[largest] < arr[r]:
        largest = r
# change root, if needed

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
        
# Heapify the root.
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
# Build a maxheap
# Since last parent will be at ((n/2)-1) we can start at that location.

    for i in range(n // 2 - 1, - 1, -1):
        heapify(arr, n, i)

# One by one extarct elements

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) # swap
        heapify(arr, i, 0)
        
# Driver code to test aboce
arr = [12,11,13,5,6,7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is: ')
for i in range(n):
    print(arr[i],end = " ")