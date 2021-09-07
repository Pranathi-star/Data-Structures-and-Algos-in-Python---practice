class Solution:
    def min_coins(self, req_amt, denoms):
        denoms.sort(reverse = True)
        res = 0
        for i in denoms:
            if req_amt < i:
                continue
            else:
                res += (req_amt // i)
                req_amt = (req_amt % i)
                if req_amt == 0:
                    break
        return res

req_amt = int(input().strip())
denoms = [int(i) for i in input().split()]
sol = Solution()
print(sol.min_coins(req_amt, denoms))
    
