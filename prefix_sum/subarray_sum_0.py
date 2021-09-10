class Solution:
    def subarray_sum_0(self, array):
        size = len(array)
        curr_sum = 0
        all_sums = set([0])

        for i in range(size):
            curr_sum += array[i]
            if curr_sum in all_sums:
                return True
            all_sums.add(curr_sum)
        return False

sol = Solution()
nums = [int(i) for i in input().split()]
print(sol.subarray_sum_0(nums))        