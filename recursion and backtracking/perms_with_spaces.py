class Solution:
    def __init__(self, input_str):
        self.res = []
        self.length = len(input_str)

    def perms_with_spaces(self, input_str, output_str = ""):
        if input_str == "":
            self.res.append(output_str)
            return
        if len(input_str) == self.length:
            op1 = output_str + input_str[0]
            input_str = input_str[1:]
            self.perms_with_spaces(input_str, op1)
            return
        else:
            op1 = output_str + input_str[0]
            op2 = output_str + " " + input_str[0]
            input_str = input_str[1:]
            self.perms_with_spaces(input_str, op1)
            self.perms_with_spaces(input_str, op2)
            return

input_str = input().strip()
str1 = Solution(input_str)
str1.perms_with_spaces(input_str)
print(str1.res)