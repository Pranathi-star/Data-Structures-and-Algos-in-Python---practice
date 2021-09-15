from heapq import heapify, heappush, heappop

class Solution:
    def frequency_sort(self, arr):
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        max_heap = []
        heapify(max_heap)
        size = len(arr)
        res = []

        for i in freq:
        
            heappush(max_heap, (-1 * freq[i], i))
        
        print(max_heap)
        while len(max_heap) > 0:
            curr = heappop(max_heap)
            res.extend(curr[0] * -1 * [curr[1]])
            
        return res
        
sol = Solution()
arr = [int(i) for i in input().split()]
print(sol.frequency_sort(arr))


