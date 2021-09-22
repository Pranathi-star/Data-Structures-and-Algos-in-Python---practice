n = int(input().strip())
arr = [int(i) for i in input().split()]
max_sum = sum(arr)
dp = []
for _ in range(n+1):
    dp.append([-1]*(max_sum + 1))

def subset_sum_poss(arr, n, max_sum):
    for i in range(n + 1):
        for j in range(max_sum + 1):
            if j == 0 and i >= 0:
                dp[i][j] = True
            if j > 0 and i == 0:
                dp[i][j] = False

    for i in range(1,n + 1):
        for j in range(1, max_sum + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

subset_sum_poss(arr, n, max_sum)
mid = max_sum // 2
for i in range(mid, -1, -1):
    if dp[n][i] == True:
        print(max_sum - 2*i)
        break




