class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));

        int prev=intervals[0][1];
        List <int[]> res = new ArrayList<>();
        res.add(intervals[0]);

        for (int i=1;i<intervals.length;i++){
            int start= intervals[i][0];
            int end= intervals[i][1];
            if (start>=prev){
                res.add(intervals[i]);
                prev=intervals[i][1];
            }
            else{
                prev=Math.min(res.get(res.size()-1)[1],end);
                res.get(res.size()-1)[1]=prev;
            }
        }
        return intervals.length-res.size();
    }
}
