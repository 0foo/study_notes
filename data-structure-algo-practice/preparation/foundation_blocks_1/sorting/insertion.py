def insertionSort(alist):
    for i in range(1, len(alist)):
        # element to be compared
        current = alist[i]
        # comparing the current element with the sorted portion and swapping
        while i > 0 and alist[i - 1] > current:
            # swap
            alist[i] = alist[i - 1]
            i = i - 1
            alist[i] = current
        print(alist)
    return alist

print(insertionSort([5,2,1,9,0,4,6]))



'''
Note: from the beginning of the array to the current iteration of the outer loop(i) is fully sorted


'''