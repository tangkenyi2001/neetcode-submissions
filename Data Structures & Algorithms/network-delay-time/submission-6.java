class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        boolean[] visited = new boolean[n+1];
        int[] cost = new int[n+1];
        for (int i=0;i<n+1;i++){
            cost[i]=Integer.MAX_VALUE;
        }
        List<List<int[]>> adjList = new ArrayList<>();
        for (int i=0;i<n+1;i++){
            adjList.add(new ArrayList<>());
        }
        for (int[] time : times){
            int source=time[0];
            int target=time[1];
            int edgeWeight=time[2];
            adjList.get(source).add(time);
        }
        // we want a min heap because we want to process items closest to the source node K first.
        // we need a current path weight, node,
        record Event(int costFromK, int node){};
        Queue<Event> minheap = new PriorityQueue<>(Comparator.comparingInt(Event::costFromK));
        minheap.offer(new Event(0,k));
        cost[k]=0;
        while (!minheap.isEmpty()){
            Event event= minheap.poll();
            int curNode = event.node();
            int curCost = event.costFromK();
            if (!visited[curNode]){
                visited[curNode]=true;
                for (int[] neighbor : adjList.get(curNode)){
                    int neighborNode = neighbor[1];
                    int edgeWeight=neighbor[2];
                    if (curCost+edgeWeight<cost[neighborNode]){
                        cost[neighborNode]=curCost+edgeWeight;
                    }
                    if (!visited[neighborNode]){
                        minheap.offer(new Event(curCost+edgeWeight,neighborNode));
                    }
                }
            }
        
            
        }
        int minTime=0;
        for (int i=1;i<n+1;i++){
            minTime=Math.max(minTime,cost[i]);
        }
        if (minTime==Integer.MAX_VALUE){
            return -1;
        }
        else{
            return minTime;
        }





    }
}
