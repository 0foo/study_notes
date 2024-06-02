### useful combinatorics equations

* Permutations: order matters
* Combinations: order does not matter



### Formula
* select r things from n possibilities
* n = super set, i.e. all of the items
* r = number of items to choose

<table>
<tr>
<th>Order?</th>
<th>Repetition?</th>
<th>Formula</th>
<th>Example(2 things from set of [1,2])</th>
</tr>
<tr>
<th>Yes (permutation)</th>
<th>No</th>
<th>n! &#247 (n−r)!</th>
<th>12,21</th>
</tr>
<tr>
<th>Yes (permutation)</th>
<th>Yes	</th>
<th>n<sup>r</sup></th>
<th>11,12,22,21</th>
</tr>
<tr>
<th>No (combination)</th>
<th>No</th>
<th>n! &#247 r!(n−r)!</th>
<th>12</th>
</tr>
<tr>
<th>No (combination)</th>
<th>Yes	</th>
<th>(n+r−1)! &#247 r!(n−1)!</th>
<th>11,22,12</th>
</tr>
</table>


### Permutations
*  Permutations with Repetition
    * When a thing has n different types ... we have n choices each time!
    * For example: choosing 3 of those things, the permutations are:
        * n × n × n
        * (n multiplied 3 times)
        * n × n × ... (r times) = n^r
    
* Permutations without Repetition
    * Example: what order could 16 pool balls be in?
    * After choosing, say, number "14" we can't choose it again.
    * So, our first choice has 16 possibilites, and our next choice has 15 possibilities, then 14, 13, 12, 11, ... etc. And the total permutations are:
    * 16 × 15 × 14 × 13 × ... = 20,922,789,888,000
    * n!
    
* Permutations select only some
    * `n!/(n − r)!`
    * where n is the number of things to choose from, and we choose r of them, no repetitions, order matters.
    * 16 pool balls
        * But maybe we don't want to choose them all, just 3 of them, and that is then:
        * 16 × 15 × 14 = 3,360
        * In other words, there are 3,360 different ways that 3 pool balls could be arranged out of 16 balls
    
### Combinations
* all unique combinations of a list, order doesn't matter
    * 2^n(n=size of the list)
    * 132 is considered the same as 123
  
* all combinations where order is considered unique
  * n!
  * 132 is considered different than 123
  * how many way 123 could be placed in order: 3! = 6
  
* combinations where repetitions matter
    * `(r + n -1)! / r!(n-1)!`
    * There are 35 ways of having 3 scoops from 5 flavors of icecream.
    * where n is the number of things to choose from, and we choose r of them, repetition allowed, order doesn't matter.
    
* binomial coefficient
    * n choose r
    * where n is the number of things to choose from, and we choose r of them, no repetition, order doesn't matter.
    * `n! / r!(n-r)!`
    * https://www.mathsisfun.com/data/binomial-distribution.html
    
### references
* https://www.mathsisfun.com/combinatorics/combinations-permutations.html
* https://www.cs.sfu.ca/~ggbaker/zju/math/perm-comb-more.html