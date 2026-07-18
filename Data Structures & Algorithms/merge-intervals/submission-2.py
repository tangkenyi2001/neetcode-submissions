class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                start,end=res.pop()
                res.append([start,max(intervals[i][1],end)])
            else:
                res.append(intervals[i])
        return res