class Solution:
    def __init__(self):
        self.res = []
    def find_triplets(self, array):
        array.sort()
        size = len(array)
        for i in range(size):
            target_sum = -1 * array[i]
            left = i + 1
            right = size - 1
            while(left < right):
                curr_sum = array[left] + array[right]
                if curr_sum == target_sum:
                    self.res.append([array[i], array[left], array[right]])
                    left += 1
                    right -= 1
                    while left < right and array[left] == array[left - 1]:
                        left += 1
                    while left < right and array[right] == array[right + 1]:
                        right -= 1
                elif curr_sum > target_sum:
                    right -= 1
                elif curr_sum < target_sum:
                    left += 1

arr = [int(i) for i in input().split()]
arr1 = Solution()
arr1.find_triplets(arr)
print(arr1.res)    