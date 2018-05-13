# Given a cost matrix cost[][] and a position (m, n) in cost[][], write a
# function that returns cost of minimum cost path to reach (m, n) from (0, 0).
# Each cell of the matrix represents a cost to traverse through that cell.
# Total cost of a path to reach (m, n) is sum of all the costs on that path
# (including both source and destination). You can only traverse down, right and
# diagonally lower cells from a given cell, i.e., from a given cell (i, j),
# cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed.
# You may assume that all costs are positive integers.


def get_min_cost(arr, m, n, x, y):
    # m -> rows
    # n -> cols
    dp = [[0 for x in range(n)] for x in range(m)]

    # inserting 1st element
    dp[0][0] = arr[0][0]

    # inserting values in rows
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    # cols
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + arr[0][i]

    for i in range(1, x):
        for j in range(1, y):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + arr[i][j]

    print(dp)
    return dp[x-1][y-1]


def rec_get_min_cost(arr, m, n):

    if m < 0 or n < 0:
        return 1000000
    elif m == 0 and n == 0:
        return arr[m][n]

    else:
        return arr[m][n] + min(rec_get_min_cost(arr, m-1, n),
                               rec_get_min_cost(arr, m, n-1),
                               rec_get_min_cost(arr, m-1, n-1))


if __name__ == "__main__":
    arr = [[x for x in range(6)]for x in range(5)]
    arr = [[1,2,3],[4,8,2],[1,5,3]]
    print(arr)
    print("Min cost path: {}".format(get_min_cost(arr, 3, 3, 3, 3)))

    print("Min cost path recursion: {}".format(rec_get_min_cost(arr, 2, 2)))

