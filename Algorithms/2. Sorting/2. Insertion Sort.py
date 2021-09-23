def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


numbers = [11, 7, 69, 17, 23, 1, 83, 13]
print("Unsorted: ",numbers)
insertionSort(numbers)
print("After Sorting ",numbers)
