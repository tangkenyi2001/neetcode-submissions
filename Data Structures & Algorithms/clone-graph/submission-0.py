"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap={}
        queue=[]
        queue.append(node)
        hashmap[node]=Node(node.val)
        while queue:
            cur=queue.pop(0)
            for i in cur.neighbors:
                if i not in hashmap:
                    hashmap[i]=Node(i.val)
                    queue.append(i)
                hashmap[i].neighbors.append(hashmap[cur])
        return hashmap[node]

        
