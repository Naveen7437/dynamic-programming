# The Longest Increasing Subsequence (LIS) problem is to find
# the length of the longest
# subsequence of a given sequence such that all elements of the subsequence
# are sorted in increasing order.

# Input  : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20


def get_lis(arr):
    m = len(arr)
    dp = [1 for i in range(m)]
    for i in range(1, m):
        for j in range(1, i):
            if arr[i] > arr[j] and dp[i] < dp[j] +1:
                dp[i] = dp[j] + 1

    # complexity O(nlog(n))
    return dp

# def rec_get_list(arr, m, )


if __name__ == "__main__":
    arr = [10,2,30,3, 40,5,6,7,8,80,100,10,11,12,13,1000,2000,1]
    final_arr = get_lis(arr)
    max = 0
    for i in final_arr:
        if i > max:
            max = i
    print(max)
