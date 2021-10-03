str1 = input().strip()
str2 = input().strip()
n1 = len(str1)
n2 = len(str2)
dp = []
for i in range(n1 + 1):
    dp.append([-1] * (n2 + 1))

def lcs(str1, str2, n1, n2):
    res = float('-inf')
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            elif str1[i - 1] != str2[j - 1]:
                dp[i][j] = 0
            res = max(res, dp[i][j])
    return res 
            
print(lcs(str1, str2, n1, n2))

