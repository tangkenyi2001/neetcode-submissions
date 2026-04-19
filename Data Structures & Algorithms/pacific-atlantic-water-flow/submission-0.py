class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #water can flow from higher to lower
        pacific=[[0]*len(heights[0]) for _ in heights]
        atlantic=[[0]*len(heights[0]) for _ in heights]

        rowlen=len(heights)
        collen=len(heights[0])

        firstrow,firstcol=0,0
        lastrow,lastcol=len(heights)-1,len(heights[0])-1

        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        pqueue=[]
        aqueue=[]
        pv=[[0]*len(heights[0]) for _ in heights]
        av=[[0]*len(heights[0]) for _ in heights]

        for i in range(rowlen):
            for j in range(collen):
                if i == firstrow or j==firstcol:
                    pacific[i][j]=1
                    pv[i][j]=1
                    pqueue.append([i,j])
                if i == lastrow or j==lastcol:
                    atlantic[i][j]=1
                    av[i][j]=1
                    aqueue.append([i,j])
        while pqueue:
            curx,cury=pqueue.pop(0)
            for x,y in dir:
                newx=curx+x
                newy=cury+y
                if  0<=newx<=lastrow and 0<=newy<=lastcol and pv[newx][newy]==0 and heights[newx][newy]>=heights[curx][cury]:
                    pv[newx][newy]=1
                    pacific[newx][newy]=1
                    pqueue.append([newx,newy])

        while aqueue:
            curx,cury=aqueue.pop(0)
            for x,y in dir:
                newx=curx+x
                newy=cury+y
                if  0<=newx<=lastrow and 0<=newy<=lastcol and av[newx][newy]==0 and heights[newx][newy]>=heights[curx][cury]:
                    av[newx][newy]=1
                    atlantic[newx][newy]=1
                    aqueue.append([newx,newy])
        res=[]
        for i in range(rowlen):
            for j in range(collen):
                if pacific[i][j]==1 and atlantic[i][j]==1:
                    res.append([i,j])
        return res
        
