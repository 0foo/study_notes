# Big O

* polyomial
O(1)	constant	fast
O(log n)	logarithmic	
O(n)	linear time	
O(n * log n)	log linear	
O(n^2)	quadratic	
O(n^3)	cubic
  
* exponential
O(2^n)	exponential	
  
* factorial
O(n!)	factorial	slow




polynomial time:
An algorithm is said to be solvable in polynomial time if the number of steps required to complete the algorithm for a given input is O(nk) for some non-negative integer k, where n is the complexity of the input.
O(nk)
ex:2n


exponential time:
an algorithm is exponential time if T(n) is bounded by O(2nk) 
ex:n^2

The difference you are probably looking for happens to be where the variable is in the equation that expresses the run time. Equations that show a polynomial time complexity have variables in the bases of their terms. Examples: n3 + 2n2 + 1. Notice n is in the base, NOT the exponent. In exponential equations, the variable is in the exponent. Examples: 2n. As said before, exponential time grows  much faster.
If n is equal to 1000 (a reasonable input for an algorithm), then notice 10003 is 1 billion, and 21000 is simply huge! For a reference, there are about 280 hydrogen atoms in the sun, this is much more than 1 billion.

### Ref's
* https://jarednielsen.com/big-o-quadratic-time-complexity/