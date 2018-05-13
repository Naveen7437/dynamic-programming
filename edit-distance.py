# Given two strings str1 and str2 and below operations that can performed on
# str1. Find minimum number of edits (operations) required to convert
#  ‘str1’ into ‘str2’
#
# Insert
# Remove
# Replace
# All of the above operations are of equal cost.
#
# Examples:
#
# Input:   str1 = "geek", str2 = "gesek"
# Output:  1
# We can convert str1 into str2 by inserting a 's'.
#
# Input:   str1 = "cat", str2 = "cut"
# Output:  1
# We can convert str1 into str2 by replacing 'a' with 'u'.
#
# Input:   str1 = "sunday", str2 = "saturday"
# Output:  3
# Last three and first characters are same.  We basically
# need to convert "un" to "atur".  This can be done using
# below three operations.
# Replace 'n' with 'r', insert t, insert a


def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i

    for j in range(1, n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):

            # this is important
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]


def recr_edit_distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return recr_edit_distance(str1, str2, m-1, n-1)

    return 1 + min(recr_edit_distance(str1, str2, m-1, n-1),
                   recr_edit_distance(str1, str2, m-1, n),
                   recr_edit_distance(str1, str2, m, n-1))


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"

    print("Minimum distance between strings: {}".format(edit_distance
                                                        (str1, str2)))

    print("Recursion - Minimum distance between strings: {}"
          "".format(recr_edit_distance(str1, str2, len(str1), len(str2))))