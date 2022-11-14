# Selection Sort is one of the simplest sorting algorithms. This algorithm gets its name from the way it iterates through the array: it selects the current smallest element, and swaps it into place.

# Here's how it works:

# Find the smallest element in the array and swap it with the first element.
# Find the second smallest element and swap with with the second element in the array.
# Find the third smallest element and swap wit with the third element in the array.
# Repeat the process of finding the next smallest element and swapping it into the correct position until the entire array is sorted.
# But, how would you write the code for finding the index of the second smallest value in an array?

# An easy way is to notice that the smallest value has already been swapped into index 0, so the problem reduces to finding the smallest element in the array starting at index 1.

# Selection sort always takes the same number of key comparisons — N(N − 1)/2.

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
        
        for j in range(ind + 1, size):
            
            if array[j] < array[min_index]:
                min_index = j
        # Swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        
arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is: ')
print(arr)

# Space Complexity:  O(n)
# Time Complexity:  O(n2)
# Sorting in Place:  Yes
# Stable:  No