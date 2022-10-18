# Quick sort is an efficient divide and conquer sorting algorithm. Average case time complexity of Quick Sort is O(nlog(n)) with worst case time complexity being O(n^2) depending on the selection of the pivot element, which divides the current array into two sub arrays.

# For instance, the time complexity of Quick Sort is approximately O(nlog(n)) when the selection of pivot divides original array into two nearly equal sized sub arrays.

# On the other hand, if the algorithm, which selects of pivot element of the input arrays, consistently outputs 2 sub arrays with a large difference in terms of array sizes, quick sort algorithm can achieve the worst case time complexity of O(n^2).

# The steps involved in Quick Sort are:

# Choose an element to serve as a pivot, in this case, the last element of the array is the pivot.
# Partitioning: Sort the array in such a manner that all elements less than the pivot are to the left, and all elements greater than the pivot are to the right.
# Call Quicksort recursively, taking into account the previous pivot to properly subdivide the left and right arrays. (A more detailed explanation can be found in the comments below)


# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

# Functio to find the partition position
def partition(array, low, high):
    
    # choose the rightmost element as pivot
    pivot = array[high]
    
    # pointer for greater element
    i = low - 1
    
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            
            # If element smaller than pivot is found
            # swap it within the greater element pointed by i
            i = i + 1
            
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    # Return the position from where partition is done
    return i + 1

# function to perform quicksort

def quickSort(array, low, high):
    if low < high:
        
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 56, 10 , 8, 99, 10102, -6, 13, 5]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order: ")
print(data)
        
            
            
    
    
    
    
    
    