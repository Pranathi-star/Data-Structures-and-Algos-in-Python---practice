class Solution:
    def comb_sum(self, idx, array, target, output, res):
        if target == 0:
            res.append(output)
            return
        for i in range(idx, len(array)):
            if i > idx and array[i] == arr[i - 1]:
                continue
            if array[i] > target:
                break
            output.append(array[i])
            self.comb_sum(i + 1, array, target - array[i], output[:], res)
            output.pop()

arr = [int(i) for i in input().split()]
arr.sort()
target = int(input().strip())
res = []
output = []
arr1 = Solution()
arr1.comb_sum(0, arr, target, output, res)
print(res)