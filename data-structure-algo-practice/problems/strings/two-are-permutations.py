
# check length this is fastest, then sort sand check equality
def are_permutations(str1, str2):
 return (len(str1) == len(str2) and sorted(str1) == sorted(str2))


def are_permutations2(str1, str2)
    hashmap = {}

    # not could use collections.defaultdict(int) here to avoid lines 12 and 13
    for i in str1:
        if i not in hashmap:
            hashmap[i] == 1
        else:
            hashmap[i] += 1

    for i in str2:
        if i not in hashmap:
            return False
        else:
            hashmap[i] -= 1

    # note could use any() here
    for i in hashmap:
        if i != 0:
            return False


    return True