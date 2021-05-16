def knapsack(weight, value, capacity, n):
    if capacity == 0 or n == 0:
        return 0
    elif(weight[n - 1] > capacity):
        return knapsack(weight, value, capacity, n - 1)
    elif(weight[n - 1] <= capacity):
        return max(knapsack(weight, value, capacity, n - 1), value[n - 1] + knapsack(weight, value, capacity - weight[n - 1], n - 1))

n = int(input().strip())
weight = [int(i) for i in input().split()]
value = [int(i) for i in input().split()]
capacity = int(input().strip())
print(knapsack(weight, value, capacity, n))