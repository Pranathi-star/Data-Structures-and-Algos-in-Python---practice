class Solution:
    def __init__(self):
        self.res = True
    
    def check_pal(self, string):
        if len(string) == 1 or len(string) == 0:
            return self.res 
        elif string[0] == string[-1]:
            self.check_pal(string[1:-1])
            return self.res
        else:
            self.res = False
            return self.res

string = input().strip()
str1 = Solution()
print(str1.check_pal(string))