from collections import deque

class Solution:
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def find_num_with_prod(self):
        current_prod, result = 1, 0
        left, right = 0, 0
        all_combs = []

        while right < len(self.array):
            current_prod *= self.array[right]

            while(current_prod >= self.k):
                current_prod /= self.array[left]
                left += 1

            result += (right - left + 1)

            temp = deque()
            for i in range(right, left - 1, -1):
                temp.appendleft(self.array[i])
                all_combs.append(list(temp))

            right += 1
             
        return result, all_combs
            
arr = [int(i) for i in input().split()]
k = int(input().strip())
arr1 = Solution(arr, k)
print(arr1.find_num_with_prod())


