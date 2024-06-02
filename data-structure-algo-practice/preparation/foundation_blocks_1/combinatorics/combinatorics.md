## Combinatorics

### Terminology

#### Combinations/Subset
* subset is same as combination
* all possible subsets/combinations formula: 2 ^ n (number of objects in parent set)
  * this includes the empty set and the full set
  * see subset calculator online
    
  #### Subset is also the same as Combination
  * A subset is any possible combination of the original set, order doesn't matter
  * EX: {1, 2, 3, 4, 5}: {3, 1} 
  * {3,1} is not a valid Subarray or Subsequence
  * A set with n elements has 2^n subsets.
  * It is worth noting that all subarrays/substrings are subsequences and all subsequences are a subset, but the reverse is not valid. 
  
  #### Subarray/Substring
  * A subarray is a slice from a contiguous array (i.e., occupy consecutive positions) and inherently maintains the order of elements. For example, the subarrays of array
  * {1, 2, 3}: {1}, {1, 2}, {1, 2, 3}, {2}, {2, 3}, {3}
  * .A substring is almost similar to a subarray, but it is in the context of strings.
  * 'apple', 'apple', 'appl', 'pple', 'app', 'ppl', 'ple', 'ap', 'pp', 'pl', 'le', 'a', 'p', 'l', 'e', ''

  #### Sub-sequence: 
  *  ordered but non-continguous
  * {A, B, C, D, E}: {A, B, D}, {A,C,D}
    
#### Permutations
* whereas in combinations {1,3,2} and {1,2,3} are considered the same, but order determines if subarray, subseq, or subset
* in permutations {1,3,2} and {1,2,3} are DIFFERENT
* formula for permutations count is n!


### Pascals Triangle, binomial coefficient, and Combinations
* https://www.mathwords.com/b/binomial_coefficients_pascal.htm



### Ref
* https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
* https://www.chegg.com/homework-help/questions-and-answers/write-code-calculate-combination-recursively-combination-recursive-formula-n-1-21-k-base-c-q61160448