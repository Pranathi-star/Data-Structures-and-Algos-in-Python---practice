class Solution:
    def first_occurrence(self, array, k):
        low, high = 0, len(array) - 1
        res = -1

        while low <= high:
            mid = low + (high - low)//2
            if array[mid] == k:
                res = mid
                high = mid - 1
            elif array[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return mid

    def last_occurrence(self, array, k):
        low, high = 0, len(array) - 1
        res = -1

        while low <= high:
            mid = low + (high - low)//2
            if array[mid] == k:
                res = mid
                low = mid + 1
            elif array[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return mid

array = [int(i) for i in input().split()]
k = int(input().strip())
sol = Solution()
print(sol.last_occurrence(array, k) - sol.first_occurrence(array, k) + 1)