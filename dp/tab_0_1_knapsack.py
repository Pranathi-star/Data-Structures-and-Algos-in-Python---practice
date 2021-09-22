def knapsack(weight, value, capacity, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weight[i - 1] > capacity:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], value[i - 1] + dp[i - 1][j - weight[i - 1]])

    return dp[n][capacity]

n = int(input().strip())
weight = [int(i) for i in input().split()]
value = [int(i) for i in input().split()]
capacity = int(input().strip())
print(knapsack(weight, value, capacity, n))