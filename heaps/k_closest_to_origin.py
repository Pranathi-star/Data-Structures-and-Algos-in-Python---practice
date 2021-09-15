from heapq import heapify, heappush, heappop

class Solution:
    def k_closest(self, mat, n, k):
        max_heap = []
        heapify(max_heap)
        res = []

        for i in range(n):
    
            heappush(max_heap, (-1 * (pow(mat[i][0], 2) + pow(mat[i][1], 2)), (mat[i][0], mat[i][1])))
            
            if len(max_heap) > k:
                heappop(max_heap)

        while len(max_heap) > 0:
            res.append(heappop(max_heap)[1])
            
        return res
        
sol = Solution()
n = int(input().strip())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().split()])
k = int(input().strip())
print(sol.k_closest(mat, n, k))


