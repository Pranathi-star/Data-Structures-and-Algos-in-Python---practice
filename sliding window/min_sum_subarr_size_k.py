class Solution:
    def min_sum_subarr(self, arr, k):
        size = len(arr)
        left = 0
        right = k - 1
        curr_sum = sum(arr[:k])
        min_sum = curr_sum
        right += 1
        while(right != size):
            curr_sum -= arr[left]
            left += 1
            curr_sum += arr[right]
            min_sum = min(min_sum, curr_sum)
            right += 1
        return min_sum

arr = Solution()
arr1 = [int(i) for i in input().split()]
k = int(input().strip())
print(arr.min_sum_subarr(arr1, k))
            

