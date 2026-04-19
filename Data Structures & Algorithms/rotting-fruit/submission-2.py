class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs
        queue=deque()
        rowlen=len(grid)
        collen=len(grid[0])
        havefresh=False
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    havefresh=True
        if not havefresh:
            return 0
        time=0
        while queue:
            qlen=len(queue)
            haverotten=False
            for _ in range(qlen):
                curx,cury = queue.popleft()
                directions=[(0,1),(1,0),(-1,0),(0,-1)]
                for x,y in directions:
                    newx,newy=curx+x,cury+y
                    if 0<=newx<rowlen and 0<=newy<collen and grid[newx][newy]==1:
                        grid[newx][newy]=2
                        haverotten=True
                        queue.append((newx,newy))
            
            if haverotten:
                time+=1
        for i in range(rowlen):
            for j in range(collen):
                if grid[i][j]==1:
                    return -1
        return time


        