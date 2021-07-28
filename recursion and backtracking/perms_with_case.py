class Solution:
    def __init__(self):
        self.res = []
    
    def perms_with_case(self, input_str, out_str = ""):
        if input_str == "":
            self.res.append(out_str)
            return
        op1 = out_str +  input_str[0].upper()
        op2 = out_str + input_str[0].lower()
        input_str = input_str[1:]
        self.perms_with_case(input_str, op1)
        self.perms_with_case(input_str, op2)
        return

input_str = input().strip()
str1 = Solution()
str1.perms_with_case(input_str)
print(str1.res)
