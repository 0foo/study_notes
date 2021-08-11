## Sorting


#### Basic Sorts
* All O(n^2)

1. bubble sort: 
	* compares two, swaps, then compares next two
	* the largest item ends up at the end
	* repeat except not comparing item at end of array
	* sorted section is at end of the array

1. selection sort: 
	* searches entire array, finds smallest element and puts it at and of sorted array at front of main array
	* searches the unsorted space and ignores the sorted space
	* sort is at the beginning of array

1. insertion sort: 
	* grabs an element and tests with previous element until its in a sorted position, grabs next element
	* sorted portion is in beginning of array


#### More efficient Advance Sorts

1. merge sort
    * Θ(n lg n) on average, O(n lg n) worst
    * https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
    * requires extra space
    
1. quicksort
    * https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html?highlight=quicksort
    * O(n log n) on average, O(n^2) worst
    
1. heapsort
    * Note: requires knowledge of a binary tree, and heap data structure
	* https://www.geeksforgeeks.org/heap-sort/

* https://medium.com/@mera.stackhouse/which-sorting-algorithms-to-know-for-the-tech-interview-654a1f619e1d


* Merge Sort vs Quick sort
  	* Merge sort may be algorithmically faster, due to hardware architectures Quicksort is superior
  	* Typically, quicksort is significantly faster in practice than other Θ(nlogn) algorithms, because its inner loop can be efficiently implemented on most architectures, and in most real-world data, it is possible to make design choices which minimize the probability of requiring quadratic time.
	* https://stackoverflow.com/questions/680541/quick-sort-vs-merge-sort







### Partitioning

* splitting an array into two parts based on a condition

* 'multi data structure'
    * two lists and iterate through and assign to either list based on a condition
    * then join the lists
    * O(n) but has added space complexity

* 'in place'
    * O(n) but removes the space complexity
    * Have two array pointers, on insertion index and one test index
        * traverse every array item with the test index and test it's partition state
            * if it meets partition state for being on the left
                * swap test index and insertion index
                * increment insertion index.
* References                
    * http://p-nand-q.com/python/algorithms/sorting/partitioning.html



* This is my personal implementation
```
def partition(in_array, less_than_value):
    insertion_index = 0
    test_index = 0
    for item in in_array:
        if in_array[test_index] < less_than_value:
            tmp = in_array[insertion_index]
            in_array[insertion_index] = in_array[test_index]
            in_array[test_index] = tmp
            insertion_index += 1
        test_index += 1
    return in_array

```
* From: http://p-nand-q.com/python/algorithms/sorting/partitioning.html
```
def partition_bf(A, pivot_value):
    items_less_than = []
    items_greater_than_or_equal = []

    for item in A:
        if item < pivot_value:
            items_less_than.append(item)
        else:
            items_greater_than_or_equal.append(item)

    A = items_less_than + items_greater_than_or_equal
    return A, len(items_less_than)
```
* Inplace from website
```
def partition_inplace_value(A, start, stop, pel_value):
    # enumerate each item
    read_index = start
    while read_index <= stop:
        item = A[read_index]

        # if the current item is less than the pivot value
        if item < pel_value:

            # swap it at the insertion position
            A[start], A[read_index] = A[read_index], A[start]

            # and move the insertion position one up
            start += 1

        read_index += 1

    return start
```
### Partitioning

* splitting an array into two parts based on a condition

* 'multi data structure'
    * two lists and iterate through and assign to either list based on a condition
    * then join the lists
    * O(n) but has added space complexity

* 'in place'
    * O(n) but removes the space complexity
    * Have two array pointers, on insertion index and one test index
        * traverse every array item with the test index and test it's partition state
            * if it meets partition state for being on the left
                * swap test index and insertion index
                * increment insertion index.
* References                
    * http://p-nand-q.com/python/algorithms/sorting/partitioning.html



* This is my personal implementation
```
def partition(in_array, less_than_value):
    insertion_index = 0
    test_index = 0
    for item in in_array:
        if in_array[test_index] < less_than_value:
            tmp = in_array[insertion_index]
            in_array[insertion_index] = in_array[test_index]
            in_array[test_index] = tmp
            insertion_index += 1
        test_index += 1
    return in_array

```
* From: http://p-nand-q.com/python/algorithms/sorting/partitioning.html
```
def partition_bf(A, pivot_value):
    items_less_than = []
    items_greater_than_or_equal = []

    for item in A:
        if item < pivot_value:
            items_less_than.append(item)
        else:
            items_greater_than_or_equal.append(item)

    A = items_less_than + items_greater_than_or_equal
    return A, len(items_less_than)
```
* Inplace from website
```
def partition_inplace_value(A, start, stop, pel_value):
    # enumerate each item
    read_index = start
    while read_index <= stop:
        item = A[read_index]

        # if the current item is less than the pivot value
        if item < pel_value:

            # swap it at the insertion position
            A[start], A[read_index] = A[read_index], A[start]

            # and move the insertion position one up
            start += 1

        read_index += 1

    return start
```
