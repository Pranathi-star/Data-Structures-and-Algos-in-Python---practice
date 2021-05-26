no_el = int(input().strip())
arr = [int(i) for i in input().split()]
target_sum = int(input().strip())
dp = [[-1] * (target_sum + 1)] * (no_el + 1)

def subset_sum(target_sum, no_el):
    if no_el == 0:
        return 0
    if target_sum == 0:
        return 1
    if dp[no_el][target_sum] != -1:
        return dp[no_el][target_sum]
    elif arr[no_el - 1] > target_sum:
        dp[no_el][target_sum] = subset_sum(target_sum, no_el - 1)
        return dp[no_el][target_sum]

    elif arr[no_el - 1] <= target_sum:
        dp[no_el][target_sum] = subset_sum(target_sum - arr[no_el - 1], no_el - 1) + subset_sum(target_sum, no_el - 1)
        return dp[no_el][target_sum]
    
print(subset_sum(target_sum, no_el))
