### Hashmap population
* can iterate through the entire a list and every item to a set or: every value + item/index/number of occurences, add to a dictionary
* then can iterate the list again and compare list items with whats in the dictionary
* can be used in two Sum problems, duplication checks, anagram finding/ existence checking
* Looking value up in a hashmap is a O(1) operation which is way better than iterating the list another O(n) time to search for a value
* use this as value frequency counter: determine if string is anagram, find first unique character, sameFrequency


### Determine if visited/exists 
* Use a set or a dictionary these are both O(1) to fetch/check existence 
* useful for simple arithmatic in an array, can put one half of the array in hashmap and check that hashmap for a sum, or difference
* You can pass an object like a node into a set/dict and use a reference to that same object to check if exists
    * x = Node(), some_set.add(x),  x in some_set
    * Under the covers, theres a field in the object that contains a unique object Id that python uses as the key


```python

# O(n)
def has_duplicates(s = [1,45,6,1,89])
    x = {}
    y = 1

    for i in s:
        if i in x:
            x[i] = 0
        else:
            x[i] += 1

    for i in x:
        if s[i] > 1
        return True

    return False
```

```python

# O(n)
def is_anagram(s, t):
    str1 = {}
    str2 = {}

    for i in s:
        if i in str1:
            str1[i] += 1
        else:
            str1[i] = 0
            
    for i in t:
        if i in str2:
            str2[i] += 1
        else:
            str2[i] = 0

    return(str1 == str2)
```

### Swapping
* Store one value in tmp variable
* there are language specific ways but this technique is portable between languages
* This also applies to references to node objects as well in linked lists or trees, etc.

```python
    tmp = in_array[j]
    in_array[j] = in_array[k]
    in_array[k] = tmp
```

### Shift/Bubble a node to the end

```python
x = [1, 2, None, 3, 4, 5]


def shift_none_node_to_end(x)
    i = 0
    j = i + 1

    while j < len(x):
        if x[i] == None:
            temp = x[j]
            x[j] = x[i]
            x[i] = temp
        
        i += 1
        j += 1

    print(x)
```

### two pointer technique
https://leetcode.com/articles/two-pointer-technique/

* One slow-runner and the other fast-runner.
    * one pointer moves ahead of the other
    * shifting node to the end, checking for cycles in linked list

* One pointer starts from the beginning while the other pointer starts from the end.
    * check palindrome, reverse array

###  multiple pointers
  * areThereDuplicates
  * averagePair
  * isSubsequence


```python
x = [1, 2, None, 3, 4, 5]


def shift_none_node_to_end(x)
    i = 0
    j = i + 1

    while j < len(x):
        if x[i] == None:
            temp = x[j]
            x[j] = x[i]
            x[i] = temp
        
        i += 1
        j += 1

    print(x)
```

```python
def is_palindrome_outward_in(self, pal_list):
    x = len(pal_list) - 1
    y = 0
    
    while y < x:
        if pal_list[x] != pal_list[y]:
            return False
        x -= 1
        y += 1
    
    return True
```

```python
def is_palindrome_inward_out(self, s):
        if len(s) == 0:
         return False

        length = len(s)
        middle = length // 2

        if length % 2 == 0:
            i = middle
            j = middle + 1
        else:
            i = middle
            j = middle
        
        while i >=0 and j <= length:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1

        return True
```   

### Partitioning an Array
* O(N) operation and is used in quickselect, quicksort 
* capitalizes on the fact that partitioning an array is O(n) while comparing every element is O(n^2)
* Numerous way to pick the partition element with accompaniying implemention
    * pick the center element 
        * easiest implementation
    * pick randomly 
        * second easiest
        * will need to swap the partition at the end
    * pick a specific number
        * need a O(n) operation to find the value
* One issue is placing the partition element in it's correct location
    * Do the partitioning then swap the location of the partition with the location of the lower pointer
    * note: no shifting is happening only swapping, so an element that is not swapped has the same order
* interesting implementation:
    * https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/quick/quicken.htm


```python
import random
def partition_random(s):
    i = 0
    j = len(s) - 1
    index = random.randint(0, len(s))
    partition = s[index]

    while i < j:
        if s[i] <= partition:
            i += 1
        if s[j] > partition:
            j -= 1

        if s[i] > s[j]:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
    
    temp = s[index]
    s[index] = s[i]
    s[i] = temp
```


### Rotate array
* two pointer technique/bubbling/swapping
* Shift all values up/down
* i.e. [1,2,3,4,5,6,7] rotated by 2 is [3,4,5,6,7,1,2]
* numerous ways to solve this
    1. can build another array and populate it, but this require O(n) additional space
    2. can bubble up 
    3. can store the value: array[0] in a temp variable then shift all the elements down one, then put that temp variable as the last value
        *  Both 2. and 3. are O(1) space as you use the same array, and O(n) time
* one trick is to take modulus of the number_rotations_requested
    * if number_rotations_requested = len(nums) that just returns the same array as it's a full rotation
    * so need the modulus/difference after all the full rotations completed


```python
def reverse(self, a, i, j):
        while i < j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
            j -= 1
            
def rotate_array(self, nums: List[int], k: int) -> None:
    #need to take modulus in case k > len(nums), 
    #if k = len(nums) that just returns the same array as it's a full rotation
    #so need the modulus/difference after all the full rotations completed
    k = k % len(nums) 
    self.reverse(nums, 0, len(nums) - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, len(nums)-1)
```



### String is balanced (for parenthesis, or for palindrom)
* used in a variety of problems 
* checks to make sure a string is balanced
* balanced string can mean different things
    * a string that has an equal number of ‘L’ and ‘R’ characters. For example, a string that looked like ‘RLRL’ would be considered to be balanced.
        * just do the same technique as checking if two strings are anagrams 
        * order doesn't matter
    * a string that has equal number and location of matching value
        * i.e. matching parenthesis and brackets
        * order DOES matter
        * use a stack!

```python
z = '([]<><>())
def balanced_parenthesis_stack(s):
    pop_val = {
        ')': '(' ,
        ']': '[',
        '>': '<'
    }
    push_val = ['(', '[', '<']
    stack = []

    for x in s:
        if x in push_val:
            stack.append(x)

        if x in pop_val:
            if stack.pop() != pop_val['x']
            return False

    return True
```


### sliding window
  * maxSubarraySum
  * minSubArrayLen
  * findLongestSubstring
  

### Sorting 
* nLog(n)
* quick sort
    * https://www.inf.hs-flensburg.de/lang/algorithmen/sortieren/quick/quicken.htm

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

