class Solution:
    def __init__(self, array):
        self.array = array
        self.squares = [0] * len(self.array)
    
    def square_sort_sorted_array(self):
        highest_square_idx = len(self.array) - 1
        left, right = 0, len(self.array) - 1
        while left < right:
            left_sq = self.array[left] * self.array[left]
            right_sq = self.array[right] * self.array[right]
            if left_sq > right_sq:
                self.squares[highest_square_idx] = left_sq
                left += 1
            elif right_sq >= left_sq:
                self.squares[highest_square_idx] = right_sq
                right -= 1
            highest_square_idx -= 1

arr = [int(i) for i in input().split()]
arr1 = Solution(arr)
arr1.square_sort_sorted_array()
print(arr1.squares)