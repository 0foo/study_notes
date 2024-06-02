def partition(in_array, partition_value, left_index, right_index):

    while left_index < right_index:
        if in_array[left_index] > partition_value and in_array[right_index] < partition_value:
            tmp = in_array[left_index]
            in_array[left_index] = in_array[right_index]
            in_array[right_index] = tmp

        if in_array[left_index] < partition_value:
            left_index += 1

        if in_array[right_index] > partition_value:
            right_index -=1


# mid value of begnning, middle, and end
def find_pivot(in_array):
    possibles = [in_array[0], in_array[(len(in_array)-1)//2], in_array[len(in_array)-1]]
    possibles.remove(max(possibles))
    possibles.remove(min(possibles))
    return possibles[0]


def quick_recurse(in_array, left_index, right_index):
    pivot = find_pivot(in_array)
    partition(in_array, pivot, left_index, right_index)
    split_index = (left_index - right_index) / 2
    quick_recurse(in_array,left_index, split_index)
    quick_recurse(in_array, split_index, right_index)

def quick(in_array):
    quick_recurse(in_array, 0, len(in_array) - 1)