# Given an array of integers, check if theres duplicates, 
# using an efficient data structure and algorithm. Also compute Time and Space complexity.  


# hashmap method 
# add every element to a hashmap, if that  element already exists in hashmap then return Fasle
def has_dupes(list):
    hashmap = {}
    for i in list:
        if i in hashmap:
            return True
        else: 
            hashmap[i] = True
    return False



# sorting method
# sort the list, and iterate through and check if current == previous
def has_dupes(in_list):
    mylist = in_list.copy()
    mylist.sort()
    print(mylist)
    previous = None
    for current in mylist:
        if current == previous:
            return True
        else:
            previous = current
    return False