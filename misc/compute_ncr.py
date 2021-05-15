def ncr(n, r):
    res = 1
    for i in range(r):
        res *= (n - i)
        res /= (i + 1)
    return res

n = int(input().strip())
r = int(input().strip())
print(ncr(n, r))
