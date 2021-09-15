from heapq import heapify, heappush, heappop

class Solution:
    def kth_smallest(self, arr, k):
        max_heap = []
        heapify(max_heap)
        size = len(arr)

        for i in range(size):
        
            heappush(max_heap, -1 * arr[i])
            
            if len(max_heap) > k:
                heappop(max_heap)

        return (-1 * max_heap[0])

sol = Solution()
arr = [int(i) for i in input().split()]
k = int(input().strip())
print(sol.kth_smallest(arr, k))


