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
        intervals.sort(Comparator.comparingInt(x->x.start));
        List <Interval> meetings = new ArrayList<>();
        if (intervals.size()==0){
            return true;
        }
        meetings.add(intervals.get(0));
        for (int i=1;i<intervals.size();i++){
            if (intervals.get(i).start<meetings.get(meetings.size()-1).end){
                return false;
            }
            else{
                meetings.add(intervals.get(i));
            }
        }
        return true;
    }   
}
