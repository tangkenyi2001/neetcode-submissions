class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap={}
        for i in tasks:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        maxheap=[]
        for i in hashmap.keys():
            maxheap.append(-1*hashmap[i])
        heapq.heapify(maxheap)
        res=0
        cooldown=[]
        while maxheap:
            for _ in range(n):
                if maxheap:
                    cur=heapq.heappop(maxheap)
                    if cur<-1:
                        cooldown.append(cur+1)
                elif not cooldown and not maxheap:
                    return res
                res+=1
            if not maxheap and cooldown:
                res+=1
            while cooldown:
                cur=cooldown.pop(0)
                heapq.heappush(maxheap,cur)          
        return res