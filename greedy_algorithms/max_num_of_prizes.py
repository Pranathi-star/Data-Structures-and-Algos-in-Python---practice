class Solution:
    def rep_k_distinct_terms(self, no_prizes):
        res = []
        for i in range(1, no_prizes):
            if no_prizes > 2 * i:
                res.append(i)
                no_prizes -= i
            else:
                res.append(no_prizes)
                break
        return res

no_prizes = int(input().strip())
sol = Solution()
print(sol.rep_k_distinct_terms(no_prizes))
    
