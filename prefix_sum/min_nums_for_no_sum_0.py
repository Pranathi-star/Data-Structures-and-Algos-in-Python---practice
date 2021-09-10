class Solution:
    def min_for_no_subarray_sum0(self, array):
        size = len(array)
        prefix_sums = [0] * size
        prefix_sums[0] = array[0]
        sums = set()
        sums.add(0)
        curr_sum = 0
        res = 0

        for i in range(1, size):
            prefix_sums[i] = array[i] + prefix_sums[i - 1]

        for i in range(0, size):
            curr_sum += array[i]
            if curr_sum in sums:
                sums = set()
                sums.add(prefix_sums[i - 1])
                res += 1
            sums.add(curr_sum)

        return res

sol = Solution()
nums = [int(i) for i in input().split()]
print(sol.min_for_no_subarray_sum0(nums))        