class Solution:
    def peak_finding(self, arr):
        size = len(arr)
        low, high = 0, size - 1
        
        while low <= high:
            mid = low + (high - low)//2

            if mid - 1 >= 0 and mid + 1 <= size - 1 and arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid
            
            elif mid - 1 < 0 and arr[mid] >= arr[mid + 1]:
                return mid
            
            elif mid + 1 > size - 1 and arr[mid] >= arr[mid - 1]:
                return mid
            
            elif mid - 1 >= 0 and arr[mid - 1] >= arr[mid]:
                high = mid - 1
                
            elif mid + 1 <= size - 1 and arr[mid + 1] >= arr[mid]:
                low = mid + 1
        
        return -1

sol = Solution()
arr = [int(i) for i in input().split()]
print(sol.peak_finding(arr))