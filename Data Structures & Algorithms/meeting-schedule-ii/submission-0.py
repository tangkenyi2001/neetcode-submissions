"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we can sort the intervals, then we have a list of rooms, we loop through the lists, if can use the room
        # we add into the list, if no rooms avail, we add a new room
        events=[]
        for interval in intervals:
            events.append([interval.start,"START"])
            events.append([interval.end,"END"])
        res=0
        rooms=0
        events.sort()
        for event in events:
            if event[1]=="START":
                rooms+=1
            else:
                rooms-=1
            res=max(res,rooms)
        return res
