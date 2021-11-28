class Solution:
    def get_power_set(self, idx, array, output, res):
        res.append(output)
        for i in range(idx, len(array)):
            if i > idx and array[i] == array[i - 1]:
                continue
            output.append(array[i])
            self.get_power_set(i + 1, array, output[:], res)
            output.pop()

arr = [int(i) for i in input().split()]
arr1 = Solution()
arr.sort()
output= []
res = []
arr1.get_power_set(0, arr, output, res)
print(res)

