import sys


def hackerlandRadioTransmitters(x, k):
    x.sort()
    m = len(x)
    i = 0
    count = 0
    while i < m:
        j = i
        try:
            while (x[j] - x[i] <= k):
                j += 1
        except:
            pass

        count += 1
        i = i + j

    return count


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)`§