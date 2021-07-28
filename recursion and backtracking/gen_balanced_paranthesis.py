class Solution:
    def __init__(self):
        self.res = []

    def balanced_parans(self, open_p, closed_p, out_str = ""):
        if open_p == 0 and closed_p == 0:
            self.res.append(out_str)
            return
        elif open_p and closed_p and closed_p == open_p:
            op = out_str + '('
            open_p -= 1
            self.balanced_parans(open_p, closed_p, op)
        elif open_p and closed_p and closed_p > open_p:
            op1 = out_str + '('
            temp1 = open_p
            temp1 -= 1
            self.balanced_parans(temp1, closed_p, op1)
            op2 = out_str + ')'
            closed_p -= 1
            self.balanced_parans(open_p, closed_p, op2)
        elif open_p == 0 and closed_p != 0:
            op = out_str + ')'
            closed_p -= 1
            self.balanced_parans(open_p, closed_p, op)

n = int(input().strip())
open_p, closed_p = n, n
parans = Solution()
parans.balanced_parans(open_p, closed_p)
print(parans.res)