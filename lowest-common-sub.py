# LCS Problem Statement: Given two sequences, find the length of longest
# subsequence present in both of them. A subsequence is a sequence that appears
# in the same relative order, but not necessarily contiguous. For example, “abc”
# “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a
#  string of length n has 2^n different possible subsequences.

# Examples:
# input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


def lcs(str1, str2, m, n):

    # checking the base condition
    if m == 0 or n == 0:
        return 0

    dp = [[0 for x in range(m+1)] for y in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


def lcs_rec(str1, str2, m, n):

    # checking the base condition
    if m == 0 or n == 0:
        return 0

    if str1[m-1] == str2[n-1]:
        return 1 + lcs_rec(str1, str2, m-1, n-1)

    return max(lcs_rec(str1, str2, m, n-1), lcs_rec(str1, str2, m-1, n))


if __name__ == "__main__":
    str1 = "FBACASR"
    str2 = "FDBDSSDFQ"
    print("Dynamic Solution: ", lcs(str1, str2, len(str1), len(str2)))
    print("Recursive Solution: ", lcs_rec(str1, str2, len(str1), len(str2)))




