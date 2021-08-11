'''
Find the smallest number of coins to meet an sum of change


'''

# iterative
# Note: recursive version can simply replace the range(sum_to_find+1) with a recursive(sum_to_find +1) call,
# and base case to make sure sum_to_find doesn't exceed the main sum

def coin_change_1(coin_list, sum_to_find):
    memo = {}

    for sub_sum in range(sum_to_find+1):
        min = float('inf')

        for coin in coin_list:
            test_val = sub_sum - coin

            # base cases
            if test_val < 0:
                continue

            if test_val == 0:
                memo[sub_sum] = 1
                break

            if test_val > 0 and test_val in memo:
                new_num = memo[test_val] + 1
                if new_num < min:
                    min = new_num


        if min < float('inf'):
            memo[sub_sum] = min

    if sum_to_find in memo:
        print(memo[sum_to_find])
    else:
        print(str(sum_to_find) + " does not exist")