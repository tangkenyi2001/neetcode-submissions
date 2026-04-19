class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree is one with n nodes and n-1 edges, and acyclic

        # 1. n nodes
        # 2. n-1 edges
        # 3. no cycles -> topo sort
        # Use adj matrix
        # reject if edges not n-1
        if n-1!=len(edges):
            return False

        adjlist=[[] for _ in range(n)]
        for i,j in edges:
            adjlist[i].append(j)
            adjlist[j].append(i)

        queue=[0]
        visited=set()
        while queue:
            cur=queue.pop(0)
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in adjlist[cur]:
                queue.append(neighbor)
        

        return len(visited)==n