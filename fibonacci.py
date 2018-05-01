

#The Fibonacci numbers are the numbers in the following integer sequence.

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,....


def fibn(num):
    dp = [0 for i in range(num)]
    dp[1] = 1

    for i in range(2, num):
        dp[i] = dp[i-1] + dp[i-2]

    return dp


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    fib_list = fibn(num)

    fib_str = " ".join(map(str, fib_list))
    print("Fibonacci numbers till 5: {}".format(fib_str))

    print("Fibonacci number on {} position: {}".format(num, fib_list[num-1]))
