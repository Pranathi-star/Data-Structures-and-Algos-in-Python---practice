class Solution:
    def __init__(self):
        self.res = []
    
    def comb_sum(self, array, target, output = []):
        if target == 0:
            self.res.append(output)
            return
        elif len(array) == 0:
            return
        if array[0] > target:
            self.comb_sum(array[1:], target, output)
            return
        else:
            op1 = output[:]
            output.append(array[0])
            op2 = output[:]
            self.comb_sum(array, target - array[0], op2)
            array = array[1:]
            self.comb_sum(array, target, op1)
            return

arr = [int(i) for i in input().split()]
target = int(input().strip())
arr1 = Solution()
arr1.comb_sum(arr, target)
print(arr1.res)