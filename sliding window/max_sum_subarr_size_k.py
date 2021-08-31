class Solution:
    def max_sum_subarr(self, arr, k):
        size = len(arr)
        left = 0
        right = k - 1
        curr_sum = sum(arr[:k])
        max_sum = curr_sum
        right += 1
        while(right != size):
            curr_sum -= arr[left]
            left += 1
            curr_sum += arr[right]
            max_sum = max(max_sum, curr_sum)
            right += 1
        return max_sum

arr = Solution()
arr1 = [int(i) for i in input().split()]
k = int(input().strip())
print(arr.max_sum_subarr(arr1, k))
            

