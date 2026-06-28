class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #basically this is trying to find shortest path from k node to all other nodes,
        #so i do dijsktra on all of 
        visited=[0]*(n+1)
        distance=[math.inf]*(n+1)
        distance[k]=0
        distance[0]=-1
        #dijsktras basically uses a priority queue, where we put in the source node, mark as visited,
        #then put all connected nodes in the priority queue, 
        hashset={}
        for i in range(1,n+1):
            hashset[i]=[]
        for ui,vi,ti in times:
            hashset[ui].append([vi,ti])

        queue=[[0,k]]
        heapq.heapify(queue)

        while queue:
            curVal,cur=heapq.heappop(queue)
            if visited[cur]:
                continue
            visited[cur]=1
            for nextNode,nodeVal in hashset[cur]:
                if distance[cur] + nodeVal < distance[nextNode]:
                    distance[nextNode]=distance[cur] + nodeVal
                    if visited[nextNode]==0:
                        heapq.heappush(queue,([distance[cur] + nodeVal,nextNode]))
                        


        if math.inf in distance:
            return -1
        else:
            return max(distance)