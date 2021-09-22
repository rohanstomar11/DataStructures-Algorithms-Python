def linearSearch(numbers, size, element):
    i = 0
    while(i < size):
        if(numbers[i] == element):
            return i
        i += 1
    return -1


numbers = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
size = len(numbers)
element = 11
pos = linearSearch(numbers, size, element)
if(pos == -1):
    print("Element is not present in the List!")
else:
    print("Element is present at position: ", pos+1)
