str1 = input().strip()
str2 = input().strip()
n1 = len(str1)
n2 = len(str2)
dp = []
for i in range(n1 + 1):
    dp.append([-1] * (n2 + 1))

def print_lcs(str1, str2, n1, n2):
    res = ""
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            elif str1[i - 1] != str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    m, n = n1, n2
    while m > 0 and n > 0:
        if str1[m - 1] == str2[n - 1]:
            res += str1[m]
            m -= 1
            n -= 1
        else:
            pass
            return dp[n1][n2] 
            
print(print_lcs(str1, str2, n1, n2))

