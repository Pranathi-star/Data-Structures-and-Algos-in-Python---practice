from collections import deque 

class Solution:
    def first_neg_in_win(self, arr, k):
        size = len(arr)
        left, right = 0, 0
        neg_nums = deque()
        res = []
        while(right < size):
            if arr[right] < 0:
                    neg_nums.append(arr[right])
                    
            if right - left + 1 < k:
                right += 1
            
            elif right - left + 1 == k:
                if len(neg_nums) == 0:
                    res.append(0)
                else:
                    res.append(neg_nums[0])
                
                right += 1
                if len(neg_nums) > 0 and arr[left] == neg_nums[0]:
                    neg_nums.popleft()
                left += 1

        return res   

arr = Solution()
arr1 = [int(i) for i in input().split()]
k = int(input().strip())
print(arr.first_neg_in_win(arr1, k))
            
