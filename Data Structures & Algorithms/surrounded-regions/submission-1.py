class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rowlen=len(board)
        collen=len(board[0])

        queue=deque()
        #add the borders O into a queue
        visited=[[0]*collen for _ in range(rowlen)]
        for i in range(rowlen):
            for j in range(collen):
                if i==0 or i==rowlen-1 or j==0 or j==collen-1:
                    if board[i][j]=='O':
                        queue.append([i,j])
                        visited[i][j]=1
        while queue:
            curi,curj=queue.popleft()
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for i,j in dir:
                newi,newj=curi+i,curj+j
                #only continue if 
                if 0<=newi<rowlen and 0<=newj<collen and board[newi][newj]=='O' and visited[newi][newj]==0:
                    queue.append([newi,newj])
                    visited[newi][newj]=1
                    board[newi][newj]="R"

        for i in range(rowlen):
            for j in range(collen):
                if i==0 or i==rowlen-1 or j==0 or j==collen-1:
                    continue
                else:
                    if board[i][j]=="O":
                        board[i][j]="X"
                    elif board[i][j]=="R":
                        board[i][j]="O"
 
                        

                    

            
