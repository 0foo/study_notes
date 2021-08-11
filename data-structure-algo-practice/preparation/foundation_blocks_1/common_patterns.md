### Swapping
* Store one value in tmp variable
* other lang specific ways but this is portable
* This also applies to references to node objects as well in linked lists or trees, etc.

```
    tmp = in_array[j]
    in_array[j] = in_array[k]
    in_array[k] = tmp
```


### Shifting/Rotate array
* Shift all values up/down
    * use tmp variable and iterate forwards/backwards
    * can: 
        1. populate tmp variable for each variable 
        2. If a hole is present just shift everything to that hole
        3. If no hole is present just create a hole by populating tmp with the start/end location then shift
* rotate is a shift but moving displaced values around the front/back of the array


### Partitioning an Array
* O(N) operation and is used in quickselect, quicksort 
* capitalizes on the fact that partitioning an array is O(n) while comparing every element is O(n^2)
* TBI


### String is balanced (for parenthesis, or for palindrom)
* used in a variety of problems 
* checks to make sure a string is balanced
* note: this can check for palindrome or valid parenthesis
```python
# method returns true if contains valid  
# parenthesis  
def isValidString(str): 
    cnt = 0
    for i in range(len(str)): 
        if (str[i] == '('): 
            cnt += 1
        elif (str[i] == ')'): 
            cnt -= 1
        if (cnt < 0): 
            return False
    return (cnt == 0)
```

### Determine if visited/exists 
* Use a set or a dictionary these are both O(1) to fetch/check existence 
* useful for simple arithmatic in an array, can put one half of the array in hashmap and check that hashmap for a sum, or difference
* You can pass an object like a node into a set/dict and use a reference to that same object to check if exists
    * x = Node(), some_set.add(x),  x in some_set
    * Under the covers, theres a field in the object that contains a unique object Id that python uses as the key
    
### frequency counter
  * determine if string is anagram
  * sameFrequency

  
### sliding window
  * maxSubarraySum
  * minSubArrayLen
  * findLongestSubstring
  

###  multiple pointers
  * areThereDuplicates
  * averagePair
  * isSubsequence

### Sorting 
* nLog(n)

### binary search if sorted
* log(n)

### quick select
* O(n)

### BFS
* uses a queue

### DFS
* uses a stack 


### Heaps: 
* used to find minimum or maximum 
* use for prioority queue
* minHeap, maxHeap

