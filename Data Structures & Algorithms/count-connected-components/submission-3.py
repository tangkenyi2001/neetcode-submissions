class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #basically what to know number of islands
        #union? loop through and union, always add to the max, should just link to the person you attach to. then u go all th way up
        

        class Union:
            def __init__(self,n:int):
                self.parent=[i for i in range(n)]
                self.rank=[1 for _ in range(n)]

            def find(self,node):
                #returns head node
                while self.parent[node]!=node:
                    node=self.parent[node]
                return node
            
            def union(self,node1,node2):
                node1set=self.find(node1)
                node2set=self.find(node2)
                
                if self.rank[node1set]>=self.rank[node2set]:
                    self.rank[node1set]+=self.rank[node2set]
                    self.parent[node2set]=node1set
                else:
                    self.rank[node2set]+=self.rank[node1set]
                    self.parent[node1set]=node2set


            def returnConnected(self):
                count=0
                for i in range(n):
                    if i==self.parent[i]:
                        count+=1
                return count

        unionfind=Union(n)
        for node1,node2 in edges:
            unionfind.union(node1,node2)
        return unionfind.returnConnected()