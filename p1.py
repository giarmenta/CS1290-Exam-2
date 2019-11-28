def game(stones):
    n = len(stones)
    dp = [[0] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = stones[i]
    for j in range(1, n):
        for i in range(n - j):
            dp[i][i + j] = max(stones[i] - dp[i + 1][i + j], stones[i + j] - dp[i][i + j - 1])
    return dp[0][-1] > 0


st = [5, 3, 4, 5]

print(game(st))
