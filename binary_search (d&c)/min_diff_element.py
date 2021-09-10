class Solution:
    def floor(self, arr, target):
        size = len(arr)
        low, high = 0, size - 1
        res = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                res = arr[mid]
                low = mid + 1
        return res
    
    def ceil(self, arr, target):
        size = len(arr)
        low, high = 0, size - 1
        res = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                res = arr[mid]
                high = mid - 1

        return res

        
    def min_diff_element(self, arr, target):
        return min(abs(target - self.floor(arr, target)), abs(target - self.ceil(arr, target)))

sol = Solution()
arr = [int(i) for i in input().split()]
target = int(input().strip())
print(sol.min_diff_element(arr, target))