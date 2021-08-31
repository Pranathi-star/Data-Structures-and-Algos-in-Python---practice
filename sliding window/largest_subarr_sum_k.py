class Solution:
    def largest_subarr_sum_k(self, arr, k):
        left, right = 0, 0
        curr_sum = 0
        size = len(arr)
        res = 0
        while right < size:
            curr_sum += arr[right]
            while curr_sum > k:
                curr_sum -= arr[left]
                left += 1
            if curr_sum == k:
                res = max(right - left + 1, res)            
            right += 1
        return res    
            
arr = [int(i) for i in input().split()]
k = int(input().strip())
arr1 = Solution()
print(arr1.largest_subarr_sum_k(arr, k))


