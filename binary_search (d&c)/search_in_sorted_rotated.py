class Solution:
    def search_in_sorted_rotated(self, array, target):
        size = len(array)
        low, high = 0, size - 1
        if array[0] < array[size - 1]:
            return array[0]
        while low <= high:
            mid = low + (high - low)//2

            if array[mid] == target:
                return mid
            
            elif array[0] <= array[mid]:
                if target >= array[0] and target < array[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            elif array[mid] <= array[size - 1]:
                if target > array[mid] and target <= array[size - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1

sol = Solution()
array = [int(i) for i in input().split()]
target = int(input().strip())
print(sol.search_in_sorted_rotated(array, target))