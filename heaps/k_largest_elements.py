from heapq import heapify, heappush, heappop

class Solution:
    def k_largest(self, arr, k):
        min_heap = []
        heapify(min_heap)
        size = len(arr)
        res = []

        for i in range(size):
        
            heappush(min_heap, arr[i])
            
            if len(min_heap) > k:
                heappop(min_heap)

        while len(min_heap) > 0:
            res.append(min_heap.pop())

        return res
        
sol = Solution()
arr = [int(i) for i in input().split()]
k = int(input().strip())
print(sol.k_largest(arr, k))


