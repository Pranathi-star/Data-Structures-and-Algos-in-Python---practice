def matrix_chain(mat_sizes, i, j):
    if i >= j:
        dp[i][j] = 0
        return dp[i][j]

    min_comps = float('inf')

    for k in range(i, j):
        ans = (matrix_chain(mat_sizes, i, k) + matrix_chain(mat_sizes, k + 1, j) + mat_sizes[i - 1] * mat_sizes[k] * mat_sizes[j])
        if ans < min_comps:
            dp[i][j] = ans

    return dp[i][j]

dp = []
for i in range(1001):
    dp.append([-1] * 1001)
mat_sizes = [int(i) for i in input().split()]
print(matrix_chain(mat_sizes, 1, len(mat_sizes) - 1))