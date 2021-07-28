class Solution:
    def __init__(self, n):
        self.res = []
        self.n = n

    def n_digit_bins(self, ones = 0, zeroes = 0, out_str = ""):
        if ones + zeroes == self.n:
            self.res.append(out_str)
            return
        if ones > zeroes:
            op1 = out_str + "0"
            temp = zeroes
            zeroes += 1
            self.n_digit_bins(ones, zeroes, op1)
            op2 = out_str + "1"
            ones += 1
            self.n_digit_bins(ones, temp, op2)
            return
        else:
            op = out_str + "1"
            ones += 1
            self.n_digit_bins(ones, zeroes, op)
            return
        
n = int(input().strip())
n1 = Solution(n)
n1.n_digit_bins()
print(n1.res)

            

