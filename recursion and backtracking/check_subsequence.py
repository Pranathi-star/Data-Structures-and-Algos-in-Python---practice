class Solution:
    def __init__(self):
        self.res = False

    def check_subsequence_or_not(self, substr, string):
        if substr == "":
            self.res = True
            return self.res
        elif string == "" and substr != "":
            return self.res
        elif string[0] == substr[0]:
            substr = substr[1:]
            string = string[1:]
            self.check_subsequence_or_not(substr, string)
            return self.res
        else:
            string = string[1:]
            self.check_subsequence_or_not(substr, string)
            return self.res

string = input().strip()
substr = input().strip()
comb1 = Solution()
comb1.check_subsequence_or_not(substr, string)
print(comb1.res)