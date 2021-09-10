class Solution:
    def search_in_nearly_sorted(self, arr, target):
        size = len(arr)
        low, high = 0, size - 1
        
        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == target:
                return mid
            
            elif mid != size - 1 and arr[mid + 1] == target:
                return mid + 1
            
            elif mid != 0 and arr[mid - 1] == target:
                return mid - 1

            elif arr[mid] < target:
                low = mid + 2

            elif arr[mid] > target:
                high = mid - 2
        
        return -1

sol = Solution()
arr = [int(i) for i in input().split()]
target = int(input().strip())
print(sol.search_in_nearly_sorted(arr, target))