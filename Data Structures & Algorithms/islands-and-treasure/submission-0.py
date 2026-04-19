class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #nearest should be bfs.

        row=len(grid)
        col=len(grid[0])
        q=[]
        inf=2**31-1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append([i,j])
        while q:
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            curx,cury=q.pop(0)
            for x,y in directions:
                nextx,nexty=curx+x,cury+y
                if nextx>=0 and nextx<row and nexty>=0 and nexty<col and grid[nextx][nexty]==inf:
                    grid[nextx][nexty]=grid[curx][cury]+1
                    q.append([nextx,nexty])
        
