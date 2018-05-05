# Given a value N, if we want to make change for N cents, and we have infinite
# supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we
# make the change? The order of coins doesn’t matter.
#
# For example, for N = 4 and S = {1,2,3}, there are four solutions:
# {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and
# S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6},
# {2,3,5} and {5,5}. So the output should be 5.


def coin_change(arr, amount):
    m = len(arr)
    dp = [0]*(amount+1)
    dp[0] = 1

    for i in arr:
        if amount % i == 0:
            dp[i] = 1

    for i in range(1, amount+1):
        for c in arr:
            if i-c > 0:
                dp[i] = max(dp[c] + dp[i-c], dp[i])

    return dp[amount]


def recr_coin_change(arr, m , amount):
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    # this should be less than and equal to , as m is count of coins
    # not the index
    if m <= 0:
        return 0

    return recr_coin_change(arr, m-1, amount) + recr_coin_change\
        (arr, m, amount - arr[m-1])


if __name__ == "__main__":
    arr = [2, 5, 3, 6]
    amount = 10
    print("Max no of ways to make change: {}".format(coin_change(arr, amount)))
    print("Recursion -  Max no of ways to make change:"
          " {}".format(recr_coin_change(arr, len(arr), amount)))
