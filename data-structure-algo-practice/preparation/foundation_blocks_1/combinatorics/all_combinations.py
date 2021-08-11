'''
Find all possible combinations in an array
'''
import time
import random


'''
O(n^2) run time due to the copy
O(n^2) space as well due to copy
'''
def all_combinations_copy_recurse(in_arr):
    count = 1 # must increase to account for empty array, which is the base case of the recursion, so never counted

    # @profile
    def recurse(in_arr, result=[]):
        nonlocal  count

        if not in_arr:
            return

        in_arr = in_arr.copy() # Note: this adds a O(n) operation

        for i in range(len(in_arr)):
            next = result + [in_arr.pop(0)]
            recurse(in_arr, next)
            count += 1

    recurse(in_arr)
    print("all_combinations_copy_recurse count:" + str(count))

'''
Same as the copy but uses an list index to avoid the copy.
'''
def all_combinations_index_recurse(in_arr):
    count = 1

    # @profile
    def recurse(result=[], index=0):
        nonlocal count
        nonlocal in_arr

        # base
        if index > len(in_arr):
            return

        # recur
        for i in range(index, len(in_arr)):
            next_result = result + [in_arr[i]]
            recurse(next_result, i + 1)
            count = count + 1

    recurse(in_arr)
    print("all_combinations_index_recurse count:" + str(count))


'''
O(n^2) due to passing by reference
No additional space complexity
'''
def all_combinations_loops(in_array):
    pass
    # can't use window because non  continguous sequences




def timed_all_combinations(size):
    in_arr = random.sample(range(1,100), size)

    start_time = time.time()
    all_combinations_copy_recurse(in_arr)
    print("---  all_combinations_copy_recurse %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    all_combinations_index_recurse(in_arr)
    print("--- all_combinations_index_recurse %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    all_combinations_loops([1,2,3,4])
    print("--- all_combinations_loops %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    timed_all_combinations(20)

