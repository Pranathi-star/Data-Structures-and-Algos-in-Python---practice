class Solution:
    def __init__(self, stack):
        self.stack = stack
        if len(self.stack) % 2 == 0:
            self.mid = len(self.stack) // 2
        else:
            self.mid = len(self.stack) // 2 + 1
        
    def del_mid_el(self):
        if len(self.stack) == self.mid:
            self.stack.pop()
            return
        top_el = self.stack.pop()
        self.del_mid_el()
        self.stack.append(top_el)
        return 
        
stack = [int(i) for i in input().split()]
stack1 = Solution(stack)
stack1.del_mid_el()
print(stack)