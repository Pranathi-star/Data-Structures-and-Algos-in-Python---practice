no_el = int(input().strip())
arr = [int(i) for i in input().split()]
target_sum = sum(arr) // 2
dp = [[-1] * (target_sum + 1)] * (no_el + 1)

def equal_sum_partition(no_el, target_sum):
    if no_el == 0:
        dp[no_el][target_sum] = False
        return dp[no_el][target_sum]
    if target_sum == 0:
        dp[no_el][target_sum] = True
        return dp[no_el][target_sum]
    if dp[no_el][target_sum] != -1:
        return dp[no_el][target_sum]
    elif arr[no_el - 1] > target_sum:
        return equal_sum_partition(no_el - 1, target_sum)
    elif arr[no_el - 1] <= target_sum:
        return equal_sum_partition(no_el - 1, target_sum - arr[no_el - 1]) or equal_sum_partition(no_el - 1, target_sum)


if sum(arr) % 2 != 0:
    print("False")
else:
    print(equal_sum_partition(no_el, target_sum))
