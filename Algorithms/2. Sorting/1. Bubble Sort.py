def bubbleSort(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if(numbers[j] > numbers[j+1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if swapped == False:
            return


num = [11, 7, 69, 17, 23, 1, 83, 13]
bubbleSort(num)
print(num)