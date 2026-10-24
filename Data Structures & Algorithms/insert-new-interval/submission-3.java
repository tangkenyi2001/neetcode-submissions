class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
       List <int[]> res = new ArrayList<>();
       for (int[] interval: intervals){
            int start=interval[0];
            int end=interval[1];
            if (newInterval == null || end<newInterval[0]){
                res.add(interval);
            }
            else if (start>newInterval[1]){
                res.add(newInterval);
                res.add(interval);
                newInterval=null;
            }
            else{
                newInterval[0]=Math.min(newInterval[0],start);
                newInterval[1]=Math.max(newInterval[1],end);
            }
        }
        if (newInterval != null) res.add(newInterval);
        return res.toArray(new int[0][]);
        

    }
}
