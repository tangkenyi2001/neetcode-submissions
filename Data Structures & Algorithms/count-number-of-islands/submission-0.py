class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        rowlength=len(grid)
        collength=len(grid[0])
        def search(row,col):
            visited[row][col]=1
            if grid[row][col]==0:
                return
            #search up
            if row-1>=0 and visited[row-1][col]==0 and grid[row-1][col]=='1':
                search(row-1,col)
            if row+1<rowlength and visited[row+1][col]==0 and grid[row+1][col]=='1':
                search(row+1,col)
            if col-1>=0 and visited[row][col-1]==0 and grid[row][col-1]=='1':
                search(row,col-1)
            if col+1<collength and visited[row][col+1]==0 and grid[row][col+1]=='1':
                search(row,col+1)
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]=='1':
                    res+=1
                    search(i,j)
                    
        return res