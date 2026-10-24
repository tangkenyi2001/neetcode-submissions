class Solution {
    public int[][] merge(int[][] intervals) {
        //sort by start time
        Arrays.sort(intervals,Comparator.comparingInt(a -> a[0]));
        List <int[]> res = new ArrayList<>();
        res.add(intervals[0]);
        for (int i=1;i<intervals.length;i++){
            if (intervals[i][0]>res.get(res.size()-1)[1]){
                res.add(intervals[i]);
            }
            else{
                res.get(res.size()-1)[1]=Math.max(res.get(res.size()-1)[1],intervals[i][1]);
            }
        }
        return res.toArray(new int[0][]);
    }
}
