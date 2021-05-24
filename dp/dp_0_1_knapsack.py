def knapsack(weight, value, capacity, n):
    if capacity == 0 or n == 0:
        return 0
    if dp[n][capacity] != -1:
        return dp[n][capacity]
    elif(weight[n - 1] > capacity):
        dp[n][capacity] = knapsack(weight, value, capacity, n - 1)
        return dp[n][capacity]
    elif(weight[n - 1] <= capacity):
        dp[n][capacity] = max(knapsack(weight, value, capacity, n - 1), value[n - 1] + knapsack(weight, value, capacity - weight[n - 1], n - 1))
        return dp[n][capacity]

n = int(input().strip())
weight = [int(i) for i in input().split()]
value = [int(i) for i in input().split()]
capacity = int(input().strip())
dp = [[-1] * (capacity + 1)] * (n + 1)

print(knapsack(weight, value, capacity, n))