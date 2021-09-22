rod_len = int(input().strip())
costs = [int(i) for i in input().split()]
lengths = list(range(1, rod_len + 1))
dp = []
for i in range(len(costs) + 1):
    dp.append([-1] * (rod_len + 1))

def max_profit_cutting(rod_len, values, lengths):
    n = len(values)
    dp = [[0 for x in range(rod_len + 1)] for x in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, rod_len + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif lengths[i - 1] > rod_len:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i][j - lengths[i - 1]])

    return dp[n][rod_len]
    
print(max_profit_cutting(rod_len, costs, lengths))