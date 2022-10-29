from random import randint

my_array = []

for _ in range(15):
    my_array.append(randint(1,100))
   
print(my_array)



def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # ========================= #
        arr[j+1] = key