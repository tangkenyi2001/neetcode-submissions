class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #naive way is to have two array
        #one for row
        #one for col
        #if ever a 0 appears, mark the thing as 1.
        # but this i o(n) space

        #to do o(1) space, I need to , this can be a two pass, on the way down I look at the things above,
        #then on the way up i look at the things below.
        rowlen=len(matrix)
        collen=len(matrix[0])
        #first pass downwards
        firstrow0=False
        firstcol0=False
        for i in range(rowlen):
            if matrix[i][0]==0:
                firstrow0=True
        for j in range(collen):
            if matrix[0][j]==0:
                firstcol0=True   
        for i in range(rowlen):
            for j in range(collen):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,rowlen):
            for j in range(1,collen):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        for i in range(rowlen):
            if firstrow0==True:
                matrix[i][0]=0
                
        for j in range(collen):
            if firstcol0==True:
                matrix[0][j]=0
            
        
        
        