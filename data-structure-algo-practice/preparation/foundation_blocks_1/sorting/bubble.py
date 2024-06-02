def bubble(in_array):
    for index, item in enumerate(in_array):
        j = 0
        k = 1
        # traverse the array
        while k < len(in_array) - index:
            # compare
            if in_array[j] > in_array[k]:
                # swap
                tmp = in_array[j]
                in_array[j] = in_array[k]
                in_array[k] = tmp
            k += 1
            j += 1
    return in_array
