class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        top,btm=0,row-1
        currow=-1
        while top<=btm:
            mid=(top+btm)//2
            if matrix[mid][0]>target:
                btm=mid-1
            elif matrix[mid][0]<target:
                currow=mid
                top=mid+1
            else:
                return True
        if currow==-1:
            return False
        left,right=0,col-1
        while left<=right:
            mid=(left+right)//2
            if matrix[currow][mid]>target:
                right=mid-1
            elif matrix[currow][mid]<target:
                left=mid+1
            else:
                return True
        return False