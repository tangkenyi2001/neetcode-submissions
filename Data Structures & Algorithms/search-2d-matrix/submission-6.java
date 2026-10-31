class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        //naive approach is that for each row, we do binary search, m*lgn
        //
        int rowlen=matrix.length;
        int collen=matrix[0].length;
        int top = 0;
        int bottom = rowlen-1;
        int mid = 0;
        while (top<=bottom){
            mid = (top+bottom)/2;
            if (matrix[mid][0]<=target && target<=matrix[mid][collen-1]){
                break;
            }
            else if (matrix[mid][0]>target){
                bottom=mid-1;
            }
            else {
                top=mid+1;
            }
        }
        if (!(matrix[mid][0]<=target && target<=matrix[mid][collen-1])){
            return false;
        }
        int left = 0;
        int right = collen-1;
        int rowIdx=mid;
        while (left<=right){
            mid = (left+right)/2;
            if (matrix[rowIdx][mid]==target){
                return true;
            }
            else if (matrix[rowIdx][mid]>target){
                right=mid-1;
            }
            else {
                left=mid+1;
            }
        }
        return false;

    }
}
