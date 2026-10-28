class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] tasksFreq = new int[26];
        record Event(int time, int taskId){};
        Queue<Event> minheap = new PriorityQueue<>((a,b)->Integer.compare(tasksFreq[b.taskId()],tasksFreq[a.taskId()]));
        Queue<Event> queue= new ArrayDeque<>();
        for (char task : tasks){
            tasksFreq[task-'A']+=1;
        }
        for (int i=0;i<26;i++){
            if (tasksFreq[i]>0){
                minheap.offer(new Event(0,i));
            }
        }
        int cycle=0;
        while (minheap.size()>0 || queue.size()>0 ){
            while (queue.size()>0 && queue.peek().time()<=cycle){
                minheap.offer(queue.poll()); 
            }
            if (minheap.size()>0 && minheap.peek().time()<=cycle){
                Event processedEvent = minheap.poll();
                tasksFreq[processedEvent.taskId()]-=1;
                if (tasksFreq[processedEvent.taskId()]>0){
                    queue.offer(new Event(cycle+n+1,processedEvent.taskId()));
                }
            }
            cycle++;
        }
        
        return cycle;
    }
}
