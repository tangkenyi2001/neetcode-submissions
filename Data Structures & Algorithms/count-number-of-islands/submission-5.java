class Solution {
    char[][]grid;
    boolean[][]visited;
    private void dfs(int i, int j){
        this.visited[i][j]=true;
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        for (int[] dir : dirs){
            int x=dir[0]+i;
            int y=dir[1]+j;
            if (0<=x && x<visited.length && 0<=y && y<this.visited[0].length && this.grid[x][y]=='1' && !this.visited[x][y]){
                dfs(x,y);
            }
        }
    }
    public int numIslands(char[][] grid) {
        int rowlen=grid.length;
        int collen=grid[0].length;
        this.visited= new boolean[rowlen][collen];
        this.grid=grid;
        int islandsCount=0;
        for (int i=0;i<rowlen;i++){
            for (int j=0; j<collen;j++){
                if (grid[i][j]=='1' && !this.visited[i][j]){
                    dfs(i,j);
                    islandsCount++;
                }
            }
        }
        return islandsCount;
    }
}
