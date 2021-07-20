class Solution:
    def __init__(self):
        self.res = 0

    def sum_of_digits(self, n):
        if len(n) == 0:
            return
        self.res += int(n[0])
        n = n[1:]
        self.sum_of_digits(n)
        return

n = int(input().strip())
num1 = Solution()
num1.sum_of_digits(str(n))
print(num1.res)

        
