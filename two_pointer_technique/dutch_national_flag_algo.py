class Solution:
    def __init__(self, array):
        self.array = array

    def sort_array(self):
        low  = 0
        mid = 0
        high = len(self.array) - 1
        while(mid < high):
            if self.array[mid] == 0:
                self.array[low], self.array[mid] = self.array[mid], self.array[low]
                low += 1
                mid += 1
            elif self.array[mid] == 1:
                mid += 1
            elif self.array[mid] == 2:
                self.array[mid], self.array[high] = self.array[high], self.array[mid]
                high -= 1

arr = [int(i) for i in input().split()]
arr1 = Solution(arr)
arr1.sort_array()
print(arr1.array)

