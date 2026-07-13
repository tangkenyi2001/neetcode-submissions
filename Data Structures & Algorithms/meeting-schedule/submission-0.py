"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #idea is that cannot have any overlaps
        #we sort it
        sortedIntervals=sorted(intervals,key=lambda x:x.start)
        for i in range(1,len(intervals)):
            if sortedIntervals[i-1].start<=sortedIntervals[i].start<sortedIntervals[i-1].end:
                #if its within the one before, theres a confict
                return False
        return True
        # time complexity=o(nlgn), due to sorting
        # space o(1)