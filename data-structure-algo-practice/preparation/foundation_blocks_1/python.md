all()/any()
---------

all:checks if all elements are True/ any:checks if any elements are True

x = [None, None]
x = [v == None for v in x]
print(all(x))




character checks
----------
i.isalpha() = return True if letter
i.isdigit() = returns True if digit
i.lower() = returns lower case



remove from list
-------
del     O(n - i)
pop     O(n - i)
remove  O(n) 

using a list as queue: has to shift array every pop/del from the beginning. O(n) operation.
x = []
x.append("somevalue")
1. y = x.pop(0)
2. y = x[0]
    del test_list[0]


python queue
--------
most efficient:

from collections import deque
queue.append(1)
x = queue.popleft()



remove multiple items from list
-----
 iterate the positions in reverse order, 
 so removing an item doesn't shift the positions of the remaining (earlier) list items.

solution 1:
idx = [n for n, x in enumerate(my_list) if x == 0]
for i in reversed(idx):
    my_list.pop(i)

solution 2:
list = [0, 0, 0, 1, 1, 0 ,0, 1, 0]

for elem in reversed(list):
    if elem == 0:
        list.remove(elem)




reference:
https://stackoverflow.com/questions/58962005/delete-elements-from-list-in-python-and-avoid-shifting