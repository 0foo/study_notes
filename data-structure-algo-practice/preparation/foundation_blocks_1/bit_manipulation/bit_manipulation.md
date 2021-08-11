#### The logic
* AND: & - return 1 only if x and y are both 1, return 0 for any thing else
* OR: | - return 0 if x and y are both 0, return 1 for anything else
* XOR: gate gives an output of 1 if either of the inputs is different, it gives 0 if they are the same. 
* XNOR gate (negated XOR) gives an output of 1 both inputs are same and 0 if both are different. 
* NOT: reverses these



#### Uses
* AND identifies 1's
* OR identifies 0's
* XNOR idenfies if both are the same
* XOR identifies if both are different


#### bitshift operators
* x << y
    * Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
* x >> y
    * Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.


### Add two numbers using only bitwise operators


```
public int getSum(int a, int b) {

        if (b == 0){
            return a;
        }

        if (a == 0){
            return b;
        }

        int add = a ^ b;
        int carry = (a&b) << 1;

        return getSum(add, carry);
    }
```

```python

# Python3 Program to add two numbers
# without using arithmetic operator
def Add(x, y):

	# Iterate till there is no carry 
	while (y != 0):
	
		# carry now contains common
		# set bits of x and y
		carry = x & y

		# Sum of bits of x and y where at
		# least one of the bits is not set
		x = x ^ y

		# Carry is shifted by one so that 
		# adding it to x gives the required sum
		y = carry << 1
	
	return x

print(Add(15, 32))


```
* Big O is:
* This function is actually O(n) worst case, big O notation references the asymptotic upper bound of the function. The upper bound of this function in the worst case is that each of your input numbers is a max int. That means the function is called a number of times equal to the number of bits in an integer. If your integer has 32 bits, then the function runs 32 times, each time executing a series of constant operations. That makes the function O(n), where n is the size of your integer
* https://stackoverflow.com/questions/44468016/java-big-o-of-bit-manipulation
* https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/




### Count number of 




### interesting references
* https://www.openbookproject.net/thinkcs/python/english2e/ch04.html