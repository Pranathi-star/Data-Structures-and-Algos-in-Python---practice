from collections import deque
class Solution:
    def max_in_k_window(self, arr, k):
        curr_max = float('-inf')
        left, right = 0, 0
        size = len(arr)
        max_terms = deque()
        res = []
        while right < size:
            if len(max_terms) == 0 or arr[right] > max_terms[-1]:
                while(len(max_terms) != 0):
                    max_terms.popleft()
            max_terms.append(arr[right])
            if right - left + 1 < k:
                right += 1
            elif right - left + 1 == k:
                res.append(max_terms[0])
                if max_terms[0] == arr[left]:
                    max_terms.popleft()
                left += 1
                right += 1
        return res

arr = [int(i) for i in input().split()]
k = int(input().strip())
arr1 = Solution()
print(arr1.max_in_k_window(arr, k))

