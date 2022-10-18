# Insertion sort is a simple sorting algorithm for a small number of elements.

# In Insertion sort, you compare the key element with the previous elements. If the previous elements are greater than the key element, then you move the previous element to the next position.

def insertionSort(arr):
    #na przedziale od indexu 1 do (rozmiar(tabeli))
    for i in range(1, len(arr)):
        
        key = arr[i]
        print(key)
        # Move elements of arr[0.. i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        # print(j)
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [2004, 105, 600, 1, 5, 28, 125, 1590]
insertionSort(arr)
lst = []
print("Sorted array is: ")
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)

# Time Complexity: O(N^2) 
# Auxiliary Space: O(1)