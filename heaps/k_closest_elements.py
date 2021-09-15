from heapq import heapify, heappush, heappop

class Solution:
    def k_closest(self, arr, k, x):
        max_heap = []
        heapify(max_heap)
        size = len(arr)
        res = []

        for i in range(size):
        
            heappush(max_heap, (-1 * abs(arr[i] - x), arr[i]))
            
            if len(max_heap) > k:
                heappop(max_heap)

        while len(max_heap) > 0:
            res.append(heappop(max_heap)[1])
            
        return res
        
sol = Solution()
arr = [int(i) for i in input().split()]
k = int(input().strip())
x = int(input().strip())
print(sol.k_closest(arr, k, x))


