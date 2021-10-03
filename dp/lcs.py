str1 = input().strip()
str2 = input().strip()
n1 = len(str1)
n2 = len(str2)
dp = []
for i in range(n1 + 1):
    dp.append([-1] * (n2 + 1))

def lcs(str1, str2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    if dp[n1][n2] != -1:
        return dp[n1][n2]
    if str1[n1 - 1] == str2[n2 - 1]:
        dp[n1][n2] = 1 + lcs(str1, str2, n1 - 1, n2 - 1)
        return dp[n1][n2]
    elif str1[n1 - 1] != str2[n2 - 1]:
        dp[n1][n2] = max(lcs(str1, str2, n1 - 1, n2), lcs(str1, str2, n1, n2 - 1))
        return dp[n1][n2]

print(lcs(str1, str2, n1, n2))

