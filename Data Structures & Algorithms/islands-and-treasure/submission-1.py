class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf=2147483647
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append([i,j,0])
        while queue:
            curx,cury,distance=queue.popleft()
            if grid[curx][cury]== -1:
                continue
            grid[curx][cury]=min(grid[curx][cury],distance)
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in directions:
                newx,newy=curx+x,cury+y
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy]==inf:
                    queue.append([newx,newy,distance+1])

            
