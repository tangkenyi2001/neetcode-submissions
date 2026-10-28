class Solution {
    public int orangesRotting(int[][] grid) {
        //1. store all rotten fruit in a queue;
        //2. process all rotten fruits using bfs. 
        //3.if there are still fresh fruits return -1
        Queue<int[]> queue = new ArrayDeque<>();
        int rowlen=grid.length;
        int collen=grid[0].length;
        boolean fresh=false;
        for (int i=0;i<rowlen;i++){
            for (int j=0;j<collen;j++) {
                if (grid[i][j]==2){
                    queue.offer(new int[]{i,j});
                }
                else if (grid[i][j]==1){
                    fresh=true;
                }
            }
        }
        if (!fresh){
            return 0;
        }
        int minutes=0;
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        // for (int[] item : queue){
        //     System.out.println(Arrays.toString(item));
        // }
 
        while (!queue.isEmpty()){
            int curLength=queue.size();
            for (int[] item : queue){
                System.out.println(Arrays.toString(item));
            }
            System.out.println("xxxx");
            for (int k=0; k<curLength;k++){
                int[] cur = queue.poll();
                int i = cur[0];
                int j = cur[1];
            
                for (int[] dir:dirs){
                    int x=dir[0]+i;
                    int y=dir[1]+j;
                    if (0<=x && x<rowlen && 0<=y && y<collen && grid[x][y]==1){
                        queue.offer(new int[]{x,y});
                        grid[x][y]=2;

                    }
                }

            }
            minutes++;
        }
        for (int i=0;i<rowlen;i++){
            for (int j=0;j<collen;j++) {
                if (grid[i][j]==1){
                    return -1;
                }
            }
        }
        return minutes-1;

    }
}
