def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]


numbers = [11, 7, 69, 17, 23, 1, 83, 13]
print("Unsorted: ", numbers)
selectionSort(numbers)
print("After Sorting ", numbers)
