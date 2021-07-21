class Solution:
    def __init__(self, array):
        self.array = array

    def remove_duplicates(self):
        next_non_dup_idx = 1
        for i in range(len(self.array)):
            if self.array[next_non_dup_idx - 1] != self.array[i]:
                self.array[next_non_dup_idx] = self.array[i]
                next_non_dup_idx += 1
        return self.array[:next_non_dup_idx]

array = [int(i) for i in input().split()]
arr1 = Solution(array)
print(arr1.remove_duplicates())




