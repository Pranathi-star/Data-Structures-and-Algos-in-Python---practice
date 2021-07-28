class Solution:
    def __init__(self):
        self.min_so_far = 10000000
    def find_closest_sum(self, target, array):
        array.sort()
        size = len(array)
        for i in range(size):
            if i > target:
                continue
            else:
                left = i + 1
                right = size - 1
                while left < right:
                    curr_sum = array[left] + array[right]
                    target_diff = target - (curr_sum + array[i])
                    if target_diff == 0:
                        return target
                    if abs(target_diff) < abs(self.min_so_far) or (abs(target_diff) == abs(self.min_so_far) and target_diff > self.min_so_far):
                        self.min_so_far = target_diff
                    if target_diff > 0:
                        left += 1
                    elif target_diff < 0:
                        right -= 1

        return target - self.min_so_far

arr = [int(i) for i in input().split()]
target = int(input().strip())
arr1 = Solution()
print(arr1.find_closest_sum(target, arr))
