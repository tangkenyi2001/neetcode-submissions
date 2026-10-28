class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        
        record Event (int val, int idx){};
        Deque<Event> stack= new ArrayDeque<>();
        int[] res =new int[temperatures.length];
        for (int i=0;i<temperatures.length;i++){
            while (!stack.isEmpty() && stack.peek().val()<temperatures[i]){
                Event cur = stack.pop();
                res[cur.idx()]=i-cur.idx();
            }
            stack.push(new Event(temperatures[i],i));
        }
        return res;
    }
}
