'''
Rotate an array
Write a function that rotates arr[] of size n by d elements.
[1,2,3,4,5,6,7]
Rotated by 2
[3,4,5,6,7,1,2]


'''


def shift_array(arr, n=1):
    for i in range(n,len(arr)):
        arr[i-n] = arr[i]


def rotate(arr, d):
    for i in range(0, d):
        if d > len(arr): break
        temp = arr[0]
        shift_array(arr)
        last_element = len(arr)-1
        arr[last_element] = temp

    return arr
