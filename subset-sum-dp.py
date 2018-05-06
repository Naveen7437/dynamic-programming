
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
    dp = [[0 for x in range(sum + 1)] for x in range(m+1)]

    # if sum is 0  then for all the sets->{} value would be 1, so setting 1st
    # column values to 1
    for i in range(m+1):
        dp[i][0] = 1

    # for subset is 0, can we can't reach to a sum, setting all values in 1st
    # row equals to 0
    for i in range(sum+1):
        dp[0][i] = 0

    for i in range(1, m+1):
        for j in range(1, sum+1):

            # if sum is less than current value of set->{}, then check if this
            # sum is achieved without using current value
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]

            # if sum is equal to current value then set 1
            if j == arr[i-1]:
                dp[i][j] = 1

            # if sum > current value of set, then
            # 1. check is same sum is achieved without using current
            #    value i.e dp[i-1][j] or
            # 2. suppose if sum is 10 and current value of set->{} is 7
            #    then check if sum 3 is "1". because adding curr value of set-{}
            #    would make it 10.
            else:
                # if current value of set->{} if greater then sum given  then
                # we can ignore
                if arr[i-1] > sum:
                    continue

                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]

    # print(dp)
    return dp[m][sum]


if __name__ == "__main__":
    arr = [8,5,2,3, 7, 33, 34]
    sum = 19

    print("subset of sum exists: {}".format(subset_sum(arr, sum)))