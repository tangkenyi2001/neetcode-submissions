class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs
        maxArea=0
        visited=set()
        def dfs(i,j):
            res=1
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in directions:
                newx,newy=x+i,y+j
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy]==1 and (newx,newy) not in visited:
                    visited.add((newx,newy))
                    res+=dfs(newx,newy)
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    visited.add((i,j))
                    area=dfs(i,j)
                    maxArea=max(maxArea,area)

        return maxArea