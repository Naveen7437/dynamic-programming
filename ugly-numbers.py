# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly
# numbers. By convention, 1 is included.
#
# Given a number n, the task is to find n’th Ugly number.
#
# Input  : n = 7
# Output : 8
#
# Input  : n = 10
# Output : 12
#
# Input  : n = 15
# Output : 24
#
# Input  : n = 150
# Output : 5832
#


def get_ugly_numbers(num):

    if not num:
        return 0

    dp = [0 for x in range(num)]
    dp[0] = 1
    i2 = i3 = i5 = 0
    multiple2 = 2
    multiple3 = 3
    multiple5 = 5

    i = 1
    while i < num:
        # import ipdb;ipdb.set_trace()
        next_multiple = min(multiple2, multiple3, multiple5)

        if next_multiple == multiple2:
             = i2+1
            dp[i] = multiple2 = next_multiple*2

        if next_multiple == multiple3:
            next_multiple = i3 + 1
            dp[i] = multiple3 = next_multiple*3

        if next_multiple == multiple5:
            next_multiple = i5 + 1
            dp[i] = multiple5 = next_multiple*5

        i += 1

    return dp


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print("Ugly numbers till {0}: {1}".format(num, get_ugly_numbers(num)))


# Python program to find n'th Ugly number

# Function to get the nth ugly number
def getNthUglyNo(n):
    ugly = [0] * n  # To store ugly numbers

    # 1 is the first ugly number
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0

    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):

        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3,
                      next_multiple_of_5)

        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2

        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    # return ugly[n] value
    return ugly[-1]






