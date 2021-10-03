arr = [int(i) for i in input().split()]
n = len(arr)

def max_sum_no_adj(arr, n):
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    return max(max_sum_no_adj(arr, n - 2) + arr[n - 1], max_sum_no_adj(arr, n - 1))

print(max_sum_no_adj(arr, n))

