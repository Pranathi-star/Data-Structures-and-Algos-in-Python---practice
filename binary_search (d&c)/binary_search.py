class Solution:
    def __init__(self):
        self.res = -1

    def binary_search(self, array, low, high, target):
        if low <= high:
            mid = low + (high - low)//2
            if array[mid] == target:
                self.res = mid
                return self.res
            elif array[mid] > target:
                return self.binary_search(array[:], low, mid - 1, target)
            else:
                return self.binary_search(array[:], mid + 1, high, target)
        else:
            return self.res

array = [int(i) for i in input().split()]
target = int(input().strip())
array.sort()
arr1 = Solution()
print(arr1.binary_search(array, 0, len(array) - 1, target))

