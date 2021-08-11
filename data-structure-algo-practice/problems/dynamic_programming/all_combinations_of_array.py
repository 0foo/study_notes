'''
Print all possible combinations of r elements in a given array of size n

Given an array of size n, generate and print all possible combinations of r elements in array.
For example, if input array is {1, 2, 3, 4} and r is 2, then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.
'''



def all_combos(base_arr, n, in_arr=[]):
    if len(in_arr) == n:
        print(in_arr)
        return

    for i in base_arr:
        in_arr.append(i)
        all_combos(base_arr, n, in_arr)


