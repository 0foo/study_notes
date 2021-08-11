## To Know
* This is a starter collection of tools/ideas to know to solve problems and for the interview
    * not comprehensive, this is a sub set of everything to know
    
### to consider 
* space vs size of data: RAM vsnHard drive
* threads
* time and space complexity

### Strategies
* preprocessing

### refresher
* logarithms
* regex

### Sorts
* the mathematical bound of comparison sort is (n log n)

### Array
* [1,2,3,4,5]
* push, append, pop all will use the END of the list i.e. number 5
* shift, unshift, pop(0), all use the beginning of the list: number 1

#### Simple sorts
1. insertion sort: explain when it can be better than the above two
    * poor efficiency best: O(n), average and worst: O(n^2)
    * differs from selection in that:
      * insertion does comparison with sorted side of array
      * selection does comparison with unsorted side
    * works well for continuous sorting, i.e. if you're constantly adding items just requires a single pass
       * bubble and selection require a search of the entire array, insertion just requires search of the sorted portion

2. bubble sort: why it's awful
   * largest values bubble to the top
   * poor efficiency best: O(n), average and worst: O(n^2)
   * in-place sort
   * builds the sort at the end of the list
  
3. selection sort: usually thrown in as an example when asked to list sorting algorithms
   * iterate through and find the smallest element and switch with the first element
   * builds the sort at the beginning of the list
   * O(n^2) for best, average, and worst
   * much less swaps than bubble sort, only make one swap per loop, vs bubble making many swaps\
   * differs from insertion in that:
      * insertion does comparison with sorted side of array
      * selection does comparison with unsorted side
  
#### Complex sorts
1. quicksort: 
   * implement it, explain it
   * in place sort
2. mergesort: 
   * implement it, talk about space complexity as well as time complexity
   * not in place sort
3. heapsort: explain how it works, and how heaps work in general
4. radix/counting/bucket sort: when it's useful
   * don't worry about implementing but learn how it works
   * this is good for sorting integers
   * it puts integers into buckets based on each digit in the integer. Each bucket is sorted, then the next digit is used.
   * Should theoretically have a runtime of n + (number of digits in the largest number to be sorted)
  
* sort stability
  * If the sorted array has equal items in the same location as non-sorted.(see article for detailed explanation)
  * Stable: Bubble Sort, Insertion Sort, Merge Sort, Count Sort. 
  * Unstable: QuickSort, Heap Sort, and Selection Sort
  * Any given sorting algo which is not stable can be modified to be stable. 
      * By changing the key comparison operation so that the comparison of two keys considers position as a factor for objects with equal keys.
  * https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important
  * https://www.geeksforgeeks.org/stability-in-sorting-algorithms/
* https://medium.com/@mera.stackhouse/which-sorting-algorithms-to-know-for-the-tech-interview-654a1f619e1d

### Searching
1. Binary Search -will use it for tons of shit O(log(n))

## Trees
* Binary Search Tree 
  * for sortable data 
  * has all values less than on one side, all values greater than on other side
  * also called BST
  * If you can effectively use a binary search tree, you can use it to sort and search any data set that fits in memory. 
  * Use inorder DFS to get back a sorted array

### Traversal
* Breadth First
  * uses queue 
  * wide trees:will take up more space in memory during the search
* Depth First
  * inorder, preorder, postorder 
  * if very deep tree: depth first could take up alot of memory during the search
  * one example: good for quickly accessing things that are in certain categories defined by the branch of the tree
  * inorder DFS: one use is for BST-> you can get all the values back in sorted fashion
  * preorder DFS: 
    * can be used to export, store,clone duplicate a tree structure, so easily reconstructed/copied
    * root node is ALWAYS first
  * 
### Heap
* Is a tree 
* Used for Priority Queue, graph traversal
* MaxBinary Heap- parent larger than both children  
* MinBinary Heap- parent smaller than both children
* No order to the children, just that children are larger or smaller 
* Left children filled out first
* As compact as possible, every left and right are filled before moving down to next level 
* A heap as a list(n is index):
  * parent = n
  * left child is at 2n + 1
  * right child is at 2n + 2
  * a child can find it's parent by (n-1) / 2
    
  * bubbling up. 
    * push/append a new item to the end of the list/array
    * bubble up to the correct location
      * compare node to parent: the index of: (n-1) / 2
      * if larger, swap
      * repeat until node is in correct location 

  * priority queue-fetch highest value(highest priority):
    * the highest priority will always rise to the top, i.e. be the root node
    * to extract the highest priority element, must grab the root element and move child up
  
  * Sink down(after extracting highest value)
    * swap the lowest element with the root
    * compare with children(index 2n + 2, 2n + 1), swap 
    * repeat
  
* Know how to use a heap, 
    * sorting: you don't need to memorize heapsort explicitly -- 
    * you already have a basic version at your disposal
    * (just stick all your values in a heap and them pull them off until the heap is empty). 

### Hashmap
* If you need unordered key/value semantics, HashMap is more efficient than any sorted structure. 

### Hashmap plus Circular Double Linked list
* Least Recently Used/Top N of a list
    * dictionary, connected/referencing nodes in a circular list that maintains N number of items in the list/dict
    * can pop and push
    * https://leetcode.com/problems/lru-cache/
  
### Check for a number if there's a bounded number of values
* If you have a bounded number of values and need to check for duplicates
    * boolean arrays
  

### Concepts
* frequency counter
  * determine if string is anagram
  * sameFrequency

  
* sliding window
  * maxSubarraySum
  * minSubArrayLen
  * findLongestSubstring
  

* multiple pointers
  * areThereDuplicates
  * averagePair
  * isSubsequence

  
* recursion
  * factorial
  * productOfArray
  * recursiveRange
  * fibonacci
  * reverse
  * isPalindrome
  * someRecursive
  * flatten
  * capitalizeFirst
  * nestedEvenSum
  * capitalizeWords
  * stringifyNumbers
  * collectStrings


### Good problems to practice
* (just get good at leetcode easy)
* Check to see if link list has cycle
* Valid Palindrome
* Happy Number
* Valid Parenthesis
* rotate matrix
* find max depth of a tree


### To know
* Simple graph algorithms like bfs and dfs
* Union - find
* How to implement / use maps ( or dictionaries ) and set data structures.
* Dynamic programming ( one of the questions I solved involved matrix chain multiplication)
* Linked lists ( a lot of questions related to this topic is Medium rated)
* Sliding window technique.
* Recursion and backtracking ( you should be good at this , although I have yet to solve a problem related to this topic in LeetCode)
* Sorting and binary search ( a lot of easy Medium level problems are based these )
* Use of priority queues as min or max heap

### Courses
* https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/#overview

### Threads to go through
* https://www.reddit.com/r/cscareerquestions/comments/ml1yp3/are_companies_asking_harder_leetcode_questions/
* https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns
* https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions
* https://www.quora.com/Are-there-any-good-resources-or-tutorials-for-dynamic-programming-DP-besides-the-TopCoder-tutorial/answer/Michal-Danil%C3%A1k


### interesting
* https://www.quora.com/What-are-the-best-programming-interview-questions-youve-ever-asked-or-been-asked

