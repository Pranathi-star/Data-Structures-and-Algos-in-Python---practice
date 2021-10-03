n = int(input().strip())
denoms = [int(i) for i in input().split()]
req = int(input().strip())
dp = []
for i in range(n + 1):
    dp.append([-1] * (req + 1))

def max_ways_change(n, req):
    
    for j in range(n + 1):
        dp[j][0] = 1

    for i in range(req + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, req + 1):
            if denoms[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            elif denoms[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - denoms[i - 1]]

    return dp[n][req]
print(max_ways_change(n, req))