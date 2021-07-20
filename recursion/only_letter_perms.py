class Solution:
    def __init__(self):
        self.res = []
    
    def only_letter_perms(self, input_str, output_str = ""):
        if input_str == "":
            self.res.append(output_str)
            return
        if input_str[0].isalpha():
            op1 = output_str + input_str[0].lower()
            op2 = output_str + input_str[0].upper()
            input_str = input_str[1:]
            self.only_letter_perms(input_str, op1)
            self.only_letter_perms(input_str, op2)
            return
        else:
            op = output_str + input_str[0]
            input_str = input_str[1:]
            self.only_letter_perms(input_str, op)
            return

input_str = input().strip()
str1 = Solution()
str1.only_letter_perms(input_str)
print(str1.res)
