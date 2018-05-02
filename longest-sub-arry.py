
# find the sum of contiguous subarray within a one-dimensional array
# of numbers which has the largest sum.


def sub_array(arr):
    m = len(arr)

    if not m:
        return 0

    dp = [0 for i in range(m)]

    dp[0] = arr[0]

    for i in range(1, m):
        if dp[i - 1] + arr[i] > arr[i]:
            dp[i] = dp[i-1] + arr[i]
        else:
            dp[i] = arr[i]


    print(dp)
    return dp


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    final_arr = sub_array(arr)
    max = 0
    for i in final_arr:
        if i > max:
            max = i
    print(max)

