import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we choose the two heaviest stones
        #we need a max heap
        #to implement a max heap we use -1*
        maxheap=[i*-1 for i in stones]
        heapq.heapify(maxheap)

        while len(maxheap)>1:
            stone1=-1*heapq.heappop(maxheap)
            stone2=-1*heapq.heappop(maxheap)
            if stone1==stone2:
                continue
            else:
                if stone1>stone2:
                    heapq.heappush(maxheap,-1*(stone1-stone2))
                else:
                    heapq.heappush(maxheap,-1*(stone2-stone1))
        if len(maxheap)>0:
            return maxheap[0]*-1
        else:
            return 0