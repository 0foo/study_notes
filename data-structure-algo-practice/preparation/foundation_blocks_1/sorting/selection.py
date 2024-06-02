def selection(in_array):
    for index1 in range(0, len(in_array)):
        minimum_index = index1
        # search
        for index2 in range(index1, len(in_array)):
            if in_array[index2] < in_array[minimum_index]:
                minimum_index = index2
        # swap
        tmp = in_array[index1]
        in_array[index1] = in_array[minimum_index]
        in_array[minimum_index] = tmp
    return in_array
