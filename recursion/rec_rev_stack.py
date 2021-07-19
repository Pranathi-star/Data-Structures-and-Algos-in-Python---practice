class Solution:
    def __init__(self, stack):
        self.stack = stack

    def insert_at_begin(self, top_el):
        if len(self.stack) == 0:
            self.stack.append(top_el)
            return
        temp = self.stack.pop()
        self.insert_at_begin(top_el)
        self.stack.append(temp)
        return

    def rev_stack(self):
        if len(self.stack) == 1 or len(stack) == 0:
            return 
        top_el = self.stack.pop()
        self.rev_stack()
        self.insert_at_begin(top_el)
        return

stack = [int(i) for i in input().split()]
stack1 = Solution(stack)
stack1.rev_stack()
print(stack)