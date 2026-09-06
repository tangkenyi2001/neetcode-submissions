from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #basically u want to convert all the captured ones into x,
        #each of the caputured one cannot reach out
        collen=len(board[0])
        rowlen=len(board)

        reachable=[[0]*collen for i in range(rowlen)]
        visited=[[0]*collen for i in range(rowlen)]
        queue=deque([])

        for i in range(rowlen):
            for j in range(collen):
                if (i==0 or i==(rowlen-1)) and board[i][j]=='O':
                    reachable[i][j]=1
                    queue.append([i,j])
                elif (j==0 or j==(collen-1)) and board[i][j]=='O':
                    queue.append([i,j])
                    reachable[i][j]=1
        print(queue)
        while queue:
            curx,cury=queue.popleft()
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            for x,y in directions:
                newx,newy=curx+x,cury+y
                if 0<=newx<rowlen and 0<=newy<collen and board[newx][newy]=='O' and visited[newx][newy]==0:
                    reachable[newx][newy]=1
                    visited[newx][newy]=1
                    queue.append([newx,newy])

        for i in range(rowlen):
            for j in range(collen):
                if board[i][j]=='O' and reachable[i][j]==0:
                    board[i][j]='X'

                

