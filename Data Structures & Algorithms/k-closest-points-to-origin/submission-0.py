import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for i in points:
            x=i[0]
            y=i[1]
            distance=math.sqrt(pow(x,2)+pow(y,2))
            minheap.append([distance,x,y])
        heapq.heapify(minheap)
        res=[]
        for _ in range(k):
            cur=heapq.heappop(minheap)
            res.append([cur[1],cur[2]])
        return res
