class Solution:
    def __init__(self, stack):
        self.stack = stack

    def insert_in_stack(self, top_el):
        if len(self.stack) == 0:
            self.stack.append(top_el)
            return
        elif top_el >= self.stack[-1]:
            self.stack.append(top_el)
            return
        temp = self.stack.pop()
        self.insert_in_stack(top_el)
        self.stack.append(temp)
        return

    def sort_stack(self):
        if len(self.stack) == 1:
            return stack
        top_el = self.stack.pop()
        sorted_arr = self.sort_stack()
        self.insert_in_stack(top_el)
        return sorted_arr
        
stack = [int(i) for i in input().split()]
stack1 = Solution(stack)
print(stack1.sort_stack())
