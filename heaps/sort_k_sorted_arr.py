from heapq import heapify, heappush, heappop

class Solution:
    def sort_k_sorted(self, arr, k):
        min_heap = []
        heapify(min_heap)
        size = len(arr)
        res = []

        for i in range(size):
        
            heappush(min_heap, arr[i])
            
            if len(min_heap) == k:
                res.append(heappop(min_heap))

        while len(min_heap) > 0:
            res.append(heappop(min_heap))
            
        return res
        
sol = Solution()
arr = [int(i) for i in input().split()]
k = int(input().strip())
print(sol.sort_k_sorted(arr, k))


