class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            stack=[(x,y)]
            visited[x][y]=1
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            while stack:
                curx,cury=stack.pop()
                for x,y in dir:
                    newx,newy=curx+x,cury+y
                    if 0<=newx<rowlen and 0<=newy<collen and grid[newx][newy]=='1' and visited[newx][newy]==0:
                        stack.append((newx,newy))
                        visited[newx][newy]=1
        rowlen=len(grid)
        collen=len(grid[0])
        visited=[[0]*collen for _ in range(rowlen)]
        numberofislands=0
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]=='1' and visited[i][j]==0:
                    dfs(i,j)
                    numberofislands+=1
        


        return numberofislands