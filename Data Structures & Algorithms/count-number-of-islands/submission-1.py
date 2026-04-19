class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        islands=0
        def dfs(curX,curY):
            direction=[(0,1),(1,0),(0,-1),(-1,0)]
            for x,y in direction:
                newX=curX+x
                newY=curY+y
                if  0<=newX<len(grid) and 0<=newY<len(grid[0]) and grid[newX][newY]=="1" and(newX,newY) not in visited:
                    visited.add((newX,newY))
                    dfs(newX,newY)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    islands+=1
            
        
        return islands