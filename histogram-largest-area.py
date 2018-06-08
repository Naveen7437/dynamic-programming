# Find the largest rectangular area possible in a given histogram where the
# largest rectangle can be made of a number of contiguous bars. For simplicity,
# assume that all bars have same width and the width is 1 unit.
#
# For example, consider the following histogram with 7 bars of heights
# {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12


# O(n^2) while iterating, over an element check its left area and right area
# and and add both of them


def get_histogram_area(arr):
    m = len(arr)

    dp = [0]*m

    for i in range(m):
        count1 = count2 = 1

        j = i-1
        # check the left side
        while j >= 0:
            if arr[j] >= arr[i]:
                count1 += 1
            else:
                break
            j -= 1

        j = i+1
        # checking the right side
        while j < m:
            if arr[j] >= arr[i]:
                count2 += 1
            else:
                break
            j += 1

        # adding both left and right side and getting max area
        dp[i] = arr[i]*(count1 + count2 - 1)
    return dp


if __name__ == "__main__":
    arr = [3,3,3,3,2,3,3,3,3,3,3]

    final_arr = get_histogram_area(arr)
    max1 = 0
    for i in final_arr:
        if i > max1:
            max1 = i

    print("Largest Area in histogram: {}".format(max1))

# stack solution





