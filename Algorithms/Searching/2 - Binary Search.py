def binarySearch(numbers, size, element):
    low = 0
    mid = 0
    high = size-1
    while(low <= high):
        mid = int((low+high)/2)
        if(numbers[mid] == element):
            return mid
        elif(numbers[mid] >= element):
            high = mid-1
        elif(numbers[mid] <= element):
            low = mid+1
    return -1


numbers = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
size = len(numbers)
element = 44
pos = binarySearch(numbers, size, element)
if(pos == -1):
    print("Element is not present in the List!")
else:
    print("Element is present at position: ", pos+1)
