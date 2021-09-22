n = int(input().strip())
arr = [int(i) for i in input().split()]
k = int(input().strip())
res = 0
max_sum = sum(arr)
dp = []
req_target = (k + max_sum) // 2
for _ in range(n+1):
    dp.append([-1]*(req_target + 1))

no_zeroes = 0
for i in arr:
    if i == 0:
        no_zeroes += 1

def subset_sum(target_sum, no_el):
    if target_sum == 0:
        dp[no_el][target_sum] = 1
        return dp[no_el][target_sum]
    if no_el == 0:
        dp[no_el][target_sum] = 0
        return dp[no_el][target_sum]
    if dp[no_el][target_sum] != -1:
        return dp[no_el][target_sum]
    elif arr[no_el - 1] > target_sum or arr[no_el - 1] == 0:
        dp[no_el][target_sum] = subset_sum(target_sum, no_el - 1)
        return dp[no_el][target_sum]

    elif arr[no_el - 1] <= target_sum:
        dp[no_el][target_sum] = subset_sum(target_sum - arr[no_el - 1], no_el - 1) + subset_sum(target_sum, no_el - 1)
        return dp[no_el][target_sum]

if k + max_sum % 2 != 0 and k <= max_sum:
    print(pow(2, no_zeroes) * subset_sum(req_target, n))




