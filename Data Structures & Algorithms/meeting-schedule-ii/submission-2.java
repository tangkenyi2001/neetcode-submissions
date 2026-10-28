/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        Map<Integer,Integer> treemap = new TreeMap<>();
        //map the net changes at the poiint of time, so start adds 1, end -1, basically a differtence array
        for (int i=0;i<intervals.size();i++){
            Interval cur = intervals.get(i);
            treemap.merge(cur.start,1,Integer::sum);
            treemap.merge(cur.end,-1,Integer::sum);
        }
        int curRooms=0;
        int maxRooms=0;
        for (Map.Entry<Integer,Integer> entry: treemap.entrySet()){
            curRooms+=entry.getValue();
            maxRooms=Math.max(maxRooms,curRooms);
        }
        return maxRooms;
        
        
        
    }
}
