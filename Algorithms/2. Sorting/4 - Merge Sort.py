def merge(arr, low, mid, high):
    N1 = mid-low+1
    N2 = high-mid

    L = [0]*N1
    R = [0]*N2

    for i in range(N1):
        L[i] = arr[low + i]

    for j in range(N2):
        R[j] = arr[mid+1+j]

    i, j, k = 0, 0, low

    while i < N1 and j < N2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < N1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < N2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, low, high):
    if (low < high):
        mid = int((low+high)/2)
        mergeSort(arr,  low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)


numbers = [11, 7, 69, 17, 23, 1, 83, 13]
print("Unsorted: ", numbers)
mergeSort(numbers, 0, len(numbers)-1)
print("After Sorting ", numbers)
