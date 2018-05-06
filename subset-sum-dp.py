
#Given a set of non-negative integers, and a value sum, determine if
#  there is a subset of the given set with sum equal to given sum.
# subset sum problem

# example:
# [2,,3,4,,5] and sum = 8


def subset_sum(arr, sum):

    m = len(arr)

    # creating 2D dp matrix
    # cols -> sum
    # rows -> arr elements

    # crating 2D matrix with 0 value
    dp = [[0 for x in range(sum + 1)] for x in range(m)]

    # if sum is 0  the for all the sets->{} value would be 1, so setting 1st
    # column values to 1
    for i in range(m):
        dp[i][0] = 1

    for i in range(m):
        for j in range(sum+1):

            # if sum is less than current value of set->{}, the check if this
            # sum is achieved without using current value
            if j < arr[i]:
                dp[i][j] = dp[i-1][j]

            # if sum is equal to current value then set 1
            if j == arr[i]:
                dp[i][j] = 1

            # if sum > current value of set, then
            # 1. check is same sum is achieved without using current
            #    value i.e dp[i-1][j] or
            # 2. suppose if sum is 10 and current value of set->{} is 7
            #    then check if sum 3 is "1". because adding curr value of set-{}
            #    would make it 10.
            else:
                dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]

    print(dp)
    return dp[m-1][sum]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9

    print("subset of sum exists: {}".format(subset_sum(arr, sum)))