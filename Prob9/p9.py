def squares(n):
    dp = [i for i in range(n + 1)]
    k = 2
    while k * k <= n:
        for i in range(k * k, n + 1):
            dp[i] = min(dp[i], dp[i - k * k] + 1)
        k += 1
    return dp[-1]


num = 13
print(squares(num))
