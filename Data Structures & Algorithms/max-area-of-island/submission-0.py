class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowlen=len(grid)
        collen=len(grid[0])
        maxarea=0
        visited=set()
        def dfs(row,col):
            if (row<0 or row>=rowlen or col<0 or col>=collen or (row,col) in visited or grid[row][col]==0):
                return 0
            visited.add((row,col))

            return (1+dfs(row+1,col)+dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1))
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==1:
                    maxarea=max(maxarea,dfs(i,j))
        return maxarea