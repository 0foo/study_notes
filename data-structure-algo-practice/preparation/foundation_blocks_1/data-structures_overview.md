* This page needs to be cleaned up

### general info 
access-searching via key or index
search-searching via value
insert-add a new node(note:add a valueless node, may require restructuring of other nodes)
delete-delete a node(remove a node, note may require restructuring of nodes)
node- a location to store data, may be either indexed or referenced


### array
access-1 (numeric index only)
search-n ()
insert-N/A
delete-N/A

pros- fast access
cons- fixed size(no insert or delete of new nodes, can only change data in existing nodes), 
	- numeric index only
	- can't insert into middle with out 



### linked list
access-n
search-n
insert-1
delete-1

pros- dynamic number of nodes, no restructuring of nodes to add a new node
cons- slower access than array, because there is no direct access index
other - can have key/value or just a value, the key is arbitrary because it's just another data entry on a node



### doubly linked list
everything same as linked list except can go in reverse



### circularly linked list
everything same as linked list except last node references the start node



### stack(LIFO)
insert-1
access-n
search-n

implemented with array or linked
uses: function calls, recursion,reverse a word, check for balanced parenthesis, undo in text editor, back in web browsers


### queue(FIFO)

implemented with array or linked list
uses: scheduling(any situation where resources are shared among multiple users and served on first come first server basis), disk/cpu scheduling, async data transfer


array set + get = Constant time O(1)
single loop = Linear time O(n)



### arrayList vs LinkedList
add(index,element) to an index within the array: n/n
	* array list => constant access to location but have to shift the array
	* linked list => have to traverse the linked list but once arrive at location easy insert by references
	* both are linear O(n)

get(index) set(index, value) => 1/n
	* Note for arrayList will have amortized constant time to allow for expansion if filled up

search(element) => n/n
	* need to travers both and compare

isEmpty() or size() => 1/1
	* both of these are stored variable in linkedlist and inherent to arrays

remove (from the end) 1 n
remove (from the beginning) n 1
remove (in general) n n


### binary tree
