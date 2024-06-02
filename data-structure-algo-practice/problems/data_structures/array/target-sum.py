#### Given an array of unique integers, return a pair of integers that sum up to a target sum. 

"""
* The simple solution is n^2 and will check every number against every other number
* The optimized solution is to sort(if not already)
* Then have a head pointer and a tail pointer
*
"""


def get_target_pair(target, list):
    list.sort()
    max_index = len(list) - 1
    for head_index in range(0, max_index + 1):
        head_value = list[head_index]
        for tail_index in range(max_index, head_index, -1):
            tail_value = list[tail_index]
            if tail_value > target:
                continue
            print(head_value, tail_value, head_value + tail_value)
            if (head_value + tail_value) == target:
                return [head_value, tail_value]