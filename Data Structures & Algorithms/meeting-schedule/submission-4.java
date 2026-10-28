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
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort((a,b)->Integer.compare(a.start,b.start));
        if (intervals.size()<=1){
            return true;
        }
        for (int i=0;i<intervals.size()-1;i++){
            int first=i;
            int second=i+1;
            if (intervals.get(second).start<intervals.get(first).end){
                return false;
            }
        }
        return true;
    }
}
