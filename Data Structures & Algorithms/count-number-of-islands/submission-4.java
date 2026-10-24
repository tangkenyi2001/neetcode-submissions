class Solution {
    char[][]grid;
    boolean[][]visited;
    public void dfs(int i, int j){
            if (i<0 || i>=this.grid.length || j<0 || j>=this.grid[0].length){
                return;
            }
            if (this.grid[i][j]=='0' || this.visited[i][j]){
                //if its water just return
                return;
            }
            this.visited[i][j]=true;
            
            dfs(i+1,j);
            dfs(i,j+1);
            dfs(i,j-1);
            dfs(i-1,j);
        }
    public int numIslands(char[][] grid) {
        int rowlen=grid.length;
        int collen=grid[0].length;
        this.grid=grid;
        this.visited=new boolean[rowlen][collen];
        int islandcount=0;
        for (int i=0;i<rowlen;i++){
            for (int j=0;j<collen;j++){
                if (this.grid[i][j]=='1' && !this.visited[i][j]){
                    dfs(i,j);
                    islandcount++;
                }
            }
        }
        return islandcount;
    }
}
