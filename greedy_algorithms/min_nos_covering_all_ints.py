class Solution:
    def min_nums_to_cover_ints(self, no_intervals, start_pts, end_pts):
        intervals = []
        for i in range(no_intervals):
            intervals.append([start_pts[i], end_pts[i]])

        intervals.sort(key = lambda x: x[1])
        max_possible_profit = 0
        res = []
        curr_res = intervals[0][1]
        for i in intervals:
            if curr_res >= i[0] and curr_res <= i[1]:
                continue
            else:
                res.append(curr_res)
                curr_res = i[1]
        res.append(curr_res)
        
        return res

no_intervals = int(input().strip())
start_pts = [int(i) for i in input().split()]
end_pts = [int(i) for i in input().split()]
sol = Solution()
print(sol.min_nums_to_cover_ints(no_intervals, start_pts, end_pts))
    
