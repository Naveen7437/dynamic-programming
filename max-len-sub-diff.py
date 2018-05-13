# Given an array of n integers. The problem is to find maximum length of the
# subsequence with difference between adjacent elements as either 0 or 1.

# Examples:
# Input : arr[] = {2, 5, 6, 3, 7, 6, 5, 8}
# Output : 5
# The subsequence is {5, 6, 7, 6, 5}
# Input : arr[] = {-2, -1, 5, -1, 4, 0, 3}
# Output : 4

# The subsequence is {-2, -1, -1, 0}


def find_max_length(arr):
    m = len(arr)
    dp = [0]*(m)

    for i in range(m):
        for j in range(i):
            if abs(arr[i] - arr[j]) in [0, 1] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    print(dp)
    return dp


if __name__ == "__main__":
    arr = [-2, -1, 5, -1, 4, 0, 3]
    final_arr = find_max_length(arr)
    max = 0
    for i in final_arr:
        if i > max:
            max = i
    print(max+1)





