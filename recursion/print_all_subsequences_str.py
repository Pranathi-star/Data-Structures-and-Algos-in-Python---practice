class Solution:
    def __init__(self):
        self.res = set()

    def generate_subsets(self, input_str, output_str = ""):
        if input_str == "":
            self.res.add(output_str)
            return
        
        op1 = output_str
        op2 = output_str + input_str[0]
        input_str = input_str[1:]
        self.generate_subsets(input_str, op1)
        self.generate_subsets(input_str, op2)
        return

input_str = input().strip()
str1 = Solution()
str1.generate_subsets(input_str)     
print(list(str1.res))  

