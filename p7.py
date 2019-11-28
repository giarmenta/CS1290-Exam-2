def br(n):
    dp = [[0] * n for x in range(n)]
    for i in range(1, n):
        for j in range(1, i+1):
            if i + j <= n:
                dp[i + j] = max(max(dp[i], i) * max(dp[j], j), dp[i + j])
    return dp[n]


k = 10
print(br(k))
