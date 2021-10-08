class Solution:
    def no_of_rotations(self, array):
        size = len(array)
        low, high = 0, size - 1
        if array[0] < array[size - 1]:
            return 0
        while low <= high:
            mid = low + (high - low)//2
            prev = (mid + size - 1) % size
            next = (mid + 1) % size
            if array[mid] < array[prev] and array[mid] < array[next]:
                return mid
            elif array[0] <= array[mid]:
                low = mid + 1
            elif array[mid] <= array[size - 1]:
                high = mid - 1
        
        return -1

sol = Solution()
array = [int(i) for i in input().split()]
print(sol.no_of_rotations(array))