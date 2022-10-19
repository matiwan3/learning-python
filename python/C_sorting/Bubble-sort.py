# Just like the way bubbles rise from the bottom of a glass, bubble sort is a simple algorithm that sorts a list, allowing either lower or higher values to bubble up to the top. The algorithm traverses a list and compares adjacent values, swapping them if they are not in the correct order.

# With a worst-case complexity of O(n^2), bubble sort is very slow compared to other sorting algorithms like quicksort. The upside is that it is one of the easiest sorting algorithms to understand and code from scratch.

# From technical perspective, bubble sort is reasonable for sorting small-sized arrays or specially when executing sort algorithms on computers with remarkably limited memory resources.

def bubbleSort(arr):
    n = len(arr)
    #optimize code, so if the array is already sorted, it doesn't need to go through the entire process
    swapped = False
    # Tracerse through all array elements
    for i in range(n-1):
        # range(n) also work but puter loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the elemen found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop
            return
        
        
# Driver code to test aboce
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
    # % d stands for decimal values. It allows us to print numbers within strings or other values. The %d operator is put where the integer is to be specified. Floating-point numbers are converted automatically to decimal values.
    
    