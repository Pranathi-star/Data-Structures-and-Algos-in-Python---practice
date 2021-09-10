class Solution:
    def max_subarr_size(self, prefix_sum, k, size):
        low, high, res = 1, size, -1

        while low <= high:
            mid = (low + high) // 2
            for choice in range(mid, size + 1):
                if prefix_sum[choice] - prefix_sum[choice - mid] > k:
                    choice -= 1
                    break
            choice += 1
            if choice == size + 1:
                low = mid + 1
                res = mid
            else:
                high = mid - 1

        return res

sol = Solution()
nums = [int(i) for i in input().split()]
size = len(nums)
prefix_sum = [0 for x in range(size + 1)]
for i in range(size):
    prefix_sum[i + 1] = prefix_sum[i] + nums[i]
k = int(input().strip())

print(sol.max_subarr_size(prefix_sum, k, size))        