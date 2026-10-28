class Solution {
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]>queue= new ArrayDeque<>();
        int rowlen=grid.length;
        int collen=grid[0].length;

        for (int i=0; i<rowlen;i++){
            for (int j=0; j<collen;j++){
                if (grid[i][j]==0){
                    queue.offer(new int[]{i,j});
                }
            }
        }
        int distance=0;
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        while (!queue.isEmpty()){
            int curlength=queue.size();
            for (int k=0;k<curlength;k++){
                int[] curArr = queue.poll();
                int i = curArr[0];
                int j = curArr[1];
                for (int[] dir : dirs){
                    int x = dir[0]+i;
                    int y = dir[1]+j;
                    if (0<=x && x<rowlen && 0<=y && y<collen && grid[x][y]==Integer.MAX_VALUE){
                        grid[x][y] = distance + 1; 
                        queue.offer(new int[]{x,y});
                    }
                }

            }
            distance++;
        }
    }
}
