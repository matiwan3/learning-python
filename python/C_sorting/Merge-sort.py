# Merge Sort is a Divide and Conquer algorithm. It divides input array in two 
# halves, calls itself for the two halves and then merges the two sorted halves.
# The major portion of the algorithm is given two sorted arrays, and we have to 
# merge them into a single sorted array. The whole process of sorting an array of N 
# integers can be summarized into three steps-

# Divide the array into two halves.
# Sort the left half and the right half using the same recurring algorithm.
# Merge the sorted halves.
# There is something known as the Two Finger Algorithm that helps us merge two 
# sorted arrays together. Using this subroutine and calling the merge sort function 
# on the array halves recursively will give us the final sorted array we are 
# looking for.

# Since this is a recursion based algorithm, we have a recurrence relation for it. 
# A recurrence relation is simply a way of representing a problem in terms of its 
# subproblems.

# T(n) = 2 * T(n / 2) + O(n)

# Putting it in plain English, we break down the subproblem into two parts at every 
# step and we have some linear amount of work that we have to do for merging the 
# two sorted halves together at each step.

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7,123412, 65, 78, 3, 32, 64, 123, 71, 234]
    print("Given array is: ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
 