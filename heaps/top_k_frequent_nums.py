from heapq import heapify, heappush, heappop

class Solution:
    def k_most_frequent(self, arr, k):
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        min_heap = []
        heapify(min_heap)
        size = len(arr)
        res = []

        for i in freq:
        
            heappush(min_heap, (freq[i], i))
            
            if len(min_heap) > k:
                heappop(min_heap)

        while len(min_heap) > 0:
            res.append(heappop(min_heap)[1])
            
        return res
        
sol = Solution()
arr = [int(i) for i in input().split()]
k = int(input().strip())
print(sol.k_most_frequent(arr, k))


