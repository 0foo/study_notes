'''
Given an array of n integers, find the third largest element. All the elements in the array are distinct integers.
Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: The third Largest element is 14


https://www.geeksforgeeks.org/third-largest-element-array-distinct-elements/
'''

# O(n) solution
def thirdLargest(arr):
    first=-1
    second=-1
    third=-1

    for i,n in enumerate(arr):
        if n > first:
            third=second
            second=first
            first=n
        elif n > second:
            third=second
            second=n
        elif n > third:
            third=n
        print(first,second,third)


    return third




