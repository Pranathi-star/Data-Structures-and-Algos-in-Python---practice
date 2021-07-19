class Solution:
    def __init__(self, n , k):
        self.n = n
        self.k = k

    def find_kth_symbol(self, n, k):
        if n == 1 and k == 1:
            return 0

        elif k <= pow(2, n - 1) // 2:
            return self.find_kth_symbol(n - 1, k)

        else:
            return abs(self.find_kth_symbol(n - 1, k - pow(2, n - 1) // 2) - 1)

n, k = [int(i) for i in input().split()]
grammar = Solution(n , k)
print(grammar.find_kth_symbol(n, k))  
        