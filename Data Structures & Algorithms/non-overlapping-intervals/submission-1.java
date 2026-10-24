class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,Comparator.comparingInt(a->a[0]));
        int currentOverlap=0;
        List <int[]> nonOverlap = new ArrayList<>();
        nonOverlap.add(intervals[0]);
        for (int i=1;i<intervals.length;i++){
            if (intervals[i][0]<nonOverlap.get(nonOverlap.size()-1)[1]){
                currentOverlap++;
                nonOverlap.get(nonOverlap.size()-1)[1]=Math.min(intervals[i][1],nonOverlap.get(nonOverlap.size()-1)[1]);
            }
            else{
                nonOverlap.add(intervals[i]);
            }
        }
        return currentOverlap;
    }
}
