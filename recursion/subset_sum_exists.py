class Solution:
    def __init__(self):
        self.res = False

    def does_subset_exist(self, array, size, target):
        if size == 0:
            return False
        elif target == 0:
            return True
        elif array[size - 1] == target:
            return True
        elif array[size - 1] > target:
            return self.does_subset_exist(array, size - 1, target)
        elif array[size - 1] < target:
            return self.does_subset_exist(array, size - 1, target - array[size - 1]) or self.does_subset_exist(array, size - 1, target)

arr = [int(i) for i in input().split()]
target = int(input().strip())
arr1 =  Solution()
print(arr1.does_subset_exist(arr, len(arr), target))