class Solution:
    def check_prime(self, num):
        if num <= 1:
            return False
        elif num in {2, 3, 5, 7}:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        else:
            r = 5
            while r * r <= num:
                if num % r == 0:
                    return False
                r += 2
                if num % r == 0:
                    return False
                r += 4
            return True

sol = Solution()
num = int(input().strip())
print(sol.check_prime(num))        