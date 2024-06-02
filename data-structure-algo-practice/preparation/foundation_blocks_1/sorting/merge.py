def combine_sorted_arrays(array1, array2, in_array):
    # combine two sorted arrays
    j = 0
    k = 0
    for i in range(0, len(in_array)):
        # print(f"i={i}, j={j}, k={k}" )
        if j >= len(array1):
            in_array[i] = array2[k]
            k += 1
            continue
        if k >= len(array2):
            in_array[i] = array1[j]
            j += 1
            continue
        if array1[j] <= array2[k]:
            in_array[i] = array1[j]
            j += 1
            continue
        if array2[k] < array1[j]:
            in_array[i] = array2[k]
            k += 1
            continue
    print(in_array)


def merge_sort(in_array):
    if len(in_array) <= 1:
        return

    # split
    split = len(in_array) // 2
    array1 = in_array[0:split]
    array2 = in_array[split:]

    # sort the splits
    merge_sort(array1)
    merge_sort(array2)

    # combine the sorts
    combine_sorted_arrays(array1, array2, in_array)
