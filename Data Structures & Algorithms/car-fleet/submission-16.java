class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // 
        record Event(int position, int speed){};
        //timeTaken is the timeTaken for it reach the destination, (target-curPostion/speed)
        List <Event> list = new ArrayList<>();
        for (int i=0;i<position.length;i++){
            list.add(new Event(position[i],speed[i]));
        }
        list.sort((e1,e2)->Integer.compare(e2.position(),e1.position()));

        Deque <Double> stack = new ArrayDeque<>();

        for (int i=0;i<list.size();i++){
            double timeTaken=(double)(target-list.get(i).position())/list.get(i).speed();
            if (!stack.isEmpty() && timeTaken<=stack.peek()){
                continue;
            }
            else{
                stack.push(timeTaken);
            }
        }

        return stack.size();


    }
}
