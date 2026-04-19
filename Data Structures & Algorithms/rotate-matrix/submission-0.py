class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top,btm,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        while top<btm:
            #should save one side
            left=top
            right=btm
            cur=[i for i in matrix[top]]
            window=btm-top+1
            for i in range(window):
                matrix[top][right-i]=matrix[top+i][left]
            for i in range(window):
                matrix[top+i][left]=matrix[btm][left+i]
            for i in range(window):
                matrix[btm][left+i]=matrix[btm-i][right]
            for i in range(window):
                matrix[top+i][right]=cur[left+i]
        
            top+=1
            btm-=1
