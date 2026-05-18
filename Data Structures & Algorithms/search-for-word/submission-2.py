from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #classic backtracking,
        #so we always go word by word, if it doesnt fit the criteria, we backtrack
        rowlen=len(board)
        collen=len(board[0])
        visited=[[0]*collen for _ in range(rowlen)]
        def backtrack(i,j,length):
            #terminating condition
            #basically should look in all directions, but I cannot go back in the same direction
            if length==len(word)-1:
                return True
            visited[i][j]=1
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for x,y in dir:
                if 0<=i+x<rowlen and 0<=j+y<collen:
                    if visited[i+x][j+y]==0 and board[i+x][j+y]==word[length+1]:
                        if backtrack(i+x,j+y,length+1):
                            return True
            visited[i][j]=0
            return
            
        length=0
        for i in range(rowlen):
            for j in range(collen):
                if board[i][j]==word[0]:
                    if backtrack(i,j,length):
                        return True
                    
        return False