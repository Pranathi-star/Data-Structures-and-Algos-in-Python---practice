class Solution:
    def equi_index(self, array):
        res = []
        size = len(array)
        prefix_left = [0] * size
        prefix_right = [0] * size

        prefix_left[0] = array[0]
        prefix_right[size - 1] = array[size - 1]

        for i in range(1, size):
            prefix_left[i] = prefix_left[i - 1] + array[i]
            prefix_right[size - 1 - i] = prefix_right[size - i] + array[size - 1 - i]
        
        for i in range(size):
            if prefix_left[i] == prefix_right[i]:
                res.append(i)
        return res

sol = Solution()
nums = [int(i) for i in input().split()]
print(sol.equi_index(nums))        