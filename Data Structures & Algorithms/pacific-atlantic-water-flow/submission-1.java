class Solution {
    boolean[][] pvisited;
    boolean[][] avisited;
    int[][] heights;

    public void dfs(int i, int j,int ocean){
        if (ocean==1){
            // if its pacific ocean
            this.pvisited[i][j]=true;
            int[][] dirs={{0,-1},{0,1},{1,0},{-1,0}};
            for (int[]dir : dirs){
                int x= i+dir[0];
                int y= j+dir[1];
                if (0<=x && x<this.pvisited.length && 0<=y && y<this.pvisited[0].length && !this.pvisited[x][y] && this.heights[i][j]<=this.heights[x][y]){
                    dfs(x,y,ocean);
                }
            }
        }
        else{
            // if its atlantic
            this.avisited[i][j]=true;
            int[][] dirs={{0,-1},{0,1},{1,0},{-1,0}};
        for (int[]dir : dirs){
            int x= i+dir[0];
            int y= j+dir[1];
            if (0<=x && x<this.avisited.length && 0<=y && y<this.avisited[0].length && !this.avisited[x][y] && this.heights[i][j]<=this.heights[x][y]){
                dfs(x,y,ocean);
            }
        }
        }
        
            

    }
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights=heights;
        // you want it such that both oceans have flowed onto the block
        // this.flow = new int[heights.length][heights[0].length];
        this.pvisited = new boolean[heights.length][heights[0].length];
        this.avisited = new boolean[heights.length][heights[0].length];
        // flow from, the outwards block inwards via dfs;
        //pacific
        for (int i=0;i<heights.length;i++){
            for (int j=0;j<heights[0].length;j++){
                if (i==0 || j==0){
                    dfs(i,j,1);
                }
                if (i==heights.length-1 || j==heights[0].length-1){
                    dfs(i,j,2);
                }
            }
        }
        List<List<Integer>>res= new ArrayList<>();
        for (int i=0;i<heights.length;i++){
            for (int j=0;j<heights[0].length;j++){
                if (this.pvisited[i][j] && this.avisited[i][j]){
                    res.add(new ArrayList<Integer>(Arrays.asList(i, j)));
                }
            }
        }
        return res;
    }
}
