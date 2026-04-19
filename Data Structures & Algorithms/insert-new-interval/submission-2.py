class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #it is overlapping if the newInterval is less than the second of the last one, and ends when the second is less than the first of the next one
        #i can insert before resolving?
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        res=[]
        for i in intervals:
            if len(res)>0 and res[-1][0]<=i[0]<=res[-1][1]:
                res[-1][1]=max(i[1],res[-1][1])
            else:
                res.append(i)
        return res