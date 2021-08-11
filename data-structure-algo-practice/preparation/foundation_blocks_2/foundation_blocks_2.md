### Bactracking


## Optimal substructure
* A problem has an optimal substructure if an optimal solution to the entire problem contains the optimal solutions to the sub-problems.
* Lends itself to recursive solutions

## Greedy Algorithms
* A global (overall) optimal solution can be reached by choosing the optimal choice at each step.
* To make a greedy algorithm, identify an optimal substructure or subproblem in the problem. Then, determine what the solution will include (for example, the largest sum, the shortest path, etc.). Create some sort of iterative way to go through all of the subproblems and build a solution.
* In problems where greedy algorithms fail, dynamic programming might be a better approach.


### Dynamic Programming
* In problems where greedy algorithms fail, dynamic programming might be a better approach.
* An important property of a problem that is being solved through dynamic programming is that it should have overlapping subproblems. This is what distinguishes DP from divide and conquer in which storing the simpler values isn't necessary.

### Divide and Conquor
1. Divide the problem into a number of subproblems that are smaller instances of the same problem.
2. Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
3. Combine the solutions to the subproblems into the solution for the original problem.

* Recursion is LIFO flavor of divide & conquer
* Can also use FIFO divide & conquer 
* or any other kind of divide & conquer
* Look into divide and conquor algorithms.
* divides the problem evenly:
  * Here's the idea (I've somewhat simplified it):
    Solving a divide and conquer problem will cost you:
    cost/level * number of levels
    If, each level, you break each sub problem into two equal sized chunks, then it will take log_2(n) levels before the sub problem size is broken into chunks of size 1.
    However, if you break each of the the sub problems into one big chunk and one small chunk, then it can take almost n levels before the sub problems are broken into chunks of size 1.
    So, dividing each of the sub problems evenly will cost you:
    log_2(n) * cost/level
    And, dividing each of the sub problems into a big chunk, and small chunk will cost you somewhere around:
    n * cost/level (which is much worse)
    So for something like quick sort (which using the idea of divide and conquer):
    It costs n per level
    When it divides the problem evenly into nearly halves, it runs in: O(n * log_2(n))
    When it divides the problem into a big chunk and small chunk, it runs in: O(n*n) i.e. O(n^2)
