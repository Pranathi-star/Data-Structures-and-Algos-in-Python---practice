class Solution:
    def n_meetings(self, no_meetings, start_pts, end_pts):
        intervals = []
        for i in range(no_meetings):
            intervals.append([start_pts[i], end_pts[i]])

        intervals.sort(key = lambda x: x[1])
        res = []
        curr_meet = intervals[0]
        for i in range(no_meetings):
            if intervals[i][0] < curr_meet[1]:
                continue

            res.append(curr_meet)
            curr_meet = intervals[i]
        res.append(curr_meet)           
        return res

no_meetings = int(input().strip())
start_pts = [int(i) for i in input().split()]
end_pts = [int(i) for i in input().split()]
sol = Solution()
print(sol.n_meetings(no_meetings, start_pts, end_pts))
    
