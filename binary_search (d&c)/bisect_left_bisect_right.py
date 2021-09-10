from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def first_occurrence_of_k(self):
        idx = bisect_left(self.array, self.k, lo = 0, hi = len(self.array))
        if idx != len(self.array) and self.array[idx] == self.k:
            return idx
        else:
            return -1

    def last_occurrence_of_k(self):
        idx = bisect_right(self.array, self.k, lo = 0, hi = len(self.array))
        idx -= 1
        if idx >= 0 and self.array[idx] == self.k:
            return idx
        else:
            return -1
            
    def largest_num_smaller_than_k(self):
        idx = bisect_left(self.array, self.k, lo = 0, hi = len(self.array))
        idx -= 1
        if idx >= 0: 
            return idx
        else:
            return -1

    def smallest_num_larger_than_k(self):
        idx = bisect_right(self.array, self.k, lo = 0, hi = len(self.array))
        if idx < len(self.array):
            return idx
        else:
            return -1

arr = [int(i) for i in input().split()]
k = int(input().strip())
arr1 = Solution(arr, k)
print(arr1.first_occurrence_of_k())
print(arr1.last_occurrence_of_k())
print(arr1.largest_num_smaller_than_k())
print(arr1.smallest_num_larger_than_k())