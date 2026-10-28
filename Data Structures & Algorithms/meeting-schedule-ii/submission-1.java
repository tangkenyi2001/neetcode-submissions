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
        record Event(int time, boolean startBoolean){};
        List<Event> queue = new ArrayList<>();
        for (int i=0;i<intervals.size();i++){
            Interval curInterval = intervals.get(i);
            queue.add(new Event(curInterval.start,true));
            queue.add(new Event(curInterval.end,false));
        }
        queue.sort(Comparator.comparingInt(Event::time).thenComparing(Event::startBoolean));
        int curRooms=0;
        int maxRooms=0;
        for (int j=0; j<queue.size();j++){
            Event curEvent = queue.get(j);
            if (curEvent.startBoolean()){
                curRooms+=1;
            }
            else{
                curRooms-=1;
            }
            maxRooms=Math.max(maxRooms,curRooms);
        }

        return maxRooms;
    }
}
