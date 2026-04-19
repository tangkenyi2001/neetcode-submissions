class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #find rotten fruits and bfs
        queue=[]
        rowlen=len(grid)
        collen=len(grid[0])
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==2:
                    queue.append((i,j))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rounds=0
        while queue:
            length=len(queue)
            for i in range(length):
                x,y=queue.pop(0)
                for xdir,ydir in directions:
                    x_updated=x+xdir
                    y_updated=y+ydir
                    if (x_updated>=0 and x_updated<rowlen) and (y_updated>=0 and y_updated<collen) and grid[x_updated][y_updated]==1:
                        grid[x_updated][y_updated]=2
                        queue.append((x_updated,y_updated))
            if queue:
                rounds+=1
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==1:
                    return -1
        return rounds