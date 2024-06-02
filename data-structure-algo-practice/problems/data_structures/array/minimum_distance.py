'''
Find the minimum distance between two numbers
Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[].
The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
'''

import sys

def minDist(arr,x,y):
    min_dist=sys.maxsize
    x_index=-1
    for i,n in enumerate(arr):
        if arr[i] == x:
            x_index = i
        if arr[i] == y:
            if x_index == -1:
                continue
            local_min = i - x_index
            if min_dist > local_min:
                min_dist = local_min

    return min_dist

