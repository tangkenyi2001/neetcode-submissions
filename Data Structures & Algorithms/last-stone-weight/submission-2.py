class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        #minheap
        while len(stones)>1:
            heavy=heapq.heappop(stones)
            secondheavy=heapq.heappop(stones)
            if heavy!=secondheavy:
                res=heavy-secondheavy
                heapq.heappush(stones,res)
        if len(stones)==1:
            return -1*stones[0]
        else:
            return 0
        