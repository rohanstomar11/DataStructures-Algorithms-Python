def countSort(arr):
    size = max(arr)

    temp = []
    for i in range(size+1):
        temp.append(0)

    for x in arr:
        temp[x] += 1

    i, j = 0, 0
    while(i < size+1):
        if(temp[i] > 0):
            arr[j] = i
            temp[i] -= 1
            j += 1
        else:
            i += 1


numbers = [9, 1, 4, 14, 4, 15, 6]
print("Unsorted: ", numbers)
countSort(numbers)
print("After Sorting ", numbers)
