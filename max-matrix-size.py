# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
#
# For example, consider the below binary matrix.
# maximum-size-square-sub-matrix-with-all-1s


def get_max_matrix(arr, m, n):
    # m -> rows
    # n -> cols
    dp = arr.copy()
    max = 0
    for i in range(1, m):
        for j in range(1, n):
            if dp[i-1][j] > 0 and dp[i][j-1] >0 and dp[i-1][j-1] > 0:
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                if dp[i][j] > max:
                    max = dp[i][j]

    print(dp)
    return max


if __name__ == "__main__":
    arr = [[0, 1, 1],
           [0, 1, 1],
           [1, 1, 1],
           ]

    print("Max size square matrix: {}".format(get_max_matrix(arr, 3, 3)))






