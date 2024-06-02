#### Find all subarrays of length N

'''

This is the basics of almost all combination problems and there's a number of ways to do it.
Be able to implement these solutions in your sleep and understand it.
The rest of these problems build on these.

The basic ideas of generating combinations is the idea of take one, leave one.
Google recursive formulas for combinations for explanation.

'''


def combo_length_n(parent_list, length, new_list=[]):

    if len(new_list) == length:
        print(new_list)
        return

    for i in range(len(parent_list)):
        tmp = new_list + [parent_list[i]]
        combo_length_n(parent_list[i+1:], length, tmp)


# n items choose k length
def combo_length_n_2(n,k):

    def combo_length_n_2_recurse(final_arr=[], i=0):
        nonlocal n, k

        if len(final_arr) == k:
            print(final_arr)
            return

        # print(final_arr)
        if i > len(n)-1:
            return

        # take 1
        take_1_final_arr = final_arr + [n[i]]
        combo_length_n_2_recurse(take_1_final_arr, i + 1)

        # don't take 1
        combo_length_n_2_recurse(final_arr, i + 1)

    combo_length_n_2_recurse()

