n = int(input().strip())
weights = [int(i) for i in input().split()]
values = [int(i) for i in input().split()]
cap = int(input().strip())
dp = []
for i in range(n + 1):
    dp.append([-1] * (cap + 1))

def unbounded_knapsack(n, cap):
    if cap == 0 or n == 0:
        return 0
    if dp[n][cap] != -1:
        return dp[n][cap]
    elif weights[n - 1] > cap:
        dp[n][cap] = unbounded_knapsack(n - 1, cap)
        return dp[n][cap]
    elif weights[n - 1] <= cap:
        dp[n][cap] = max(unbounded_knapsack(n - 1, cap), values[n - 1] + unbounded_knapsack(n, cap - weights[n - 1]))
        return dp[n][cap]

print(unbounded_knapsack(n, cap))


