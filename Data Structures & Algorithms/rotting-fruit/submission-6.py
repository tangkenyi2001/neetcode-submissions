class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes=0
        rowlen=len(grid)
        collen=len(grid[0])
        queue=[]
        rotten=False
        fresh=False
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==1:
                    fresh=True
                if grid[i][j]==2:
                    rotten=True
                    queue.append([i,j])
        if not rotten and fresh:
            return -1
        if not rotten:
            return 0
        while queue:
            curlength=len(queue)
            for i in range(curlength):
                curx,cury=queue.pop(0)
                directions=[(0,1),(1,0),(-1,0),(0,-1)]
                for x,y in directions:
                    newx,newy=curx+x,cury+y
                    if 0<=newx<rowlen and 0<=newy<collen and grid[newx][newy]==1:
                        queue.append([newx,newy])
                        grid[newx][newy]=2
            minutes+=1
            
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==1:
                    return -1
        return minutes-1
