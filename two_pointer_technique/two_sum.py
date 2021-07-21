class Solution:
    def __init__(self, target, array):
        self.target = target
        self.array = array
    
    def target_sum(self):
        self.array.sort()
        start_ptr = 0
        end_ptr = len(self.array) - 1
        while(start_ptr != end_ptr):
            current_sum = array[start_ptr] + array[end_ptr]
            if current_sum == self.target:
                return [start_ptr, end_ptr]
            elif current_sum > self.target:
                end_ptr -= 1
            elif current_sum < self.target:
                start_ptr += 1
            if start_ptr == end_ptr:
                return [-1, -1]
        
array = [int(i) for i in input().split()]
target = int(input().strip())
comb1 = Solution(target, array)
print(comb1.target_sum())
