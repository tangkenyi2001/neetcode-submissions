class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        //basically ill use this array to mark number of items that depend on this.
        //also have a hashmap that maps a course -> List[courses] b->[a]
        Map<Integer,List<Integer>> hashmap = new HashMap<>();
        for (int i=0;i<numCourses;i++){
            hashmap.put(i,new ArrayList<>());
        }
        for (int[] prerequisite:prerequisites){
            int preReq = prerequisite[1];
            int postReq = prerequisite[0];
            indegree[postReq]+=1;
            hashmap.get(preReq).add(postReq);
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i=0;i<numCourses;i++){
            if (indegree[i]==0){
                queue.offer(i);
            }
        }
        while (!queue.isEmpty()){
            int processedCourse = queue.poll();
            List<Integer> relatedCourses=hashmap.get(processedCourse);
            for (int i=0;i<relatedCourses.size();i++){
                int relatedcourse=relatedCourses.get(i);
                indegree[relatedcourse]-=1;
                if (indegree[relatedcourse]==0){
                    queue.offer(relatedcourse);
                }
            }
        }
        for (int i=0;i<numCourses;i++){
            if (indegree[i]!=0){
                return false;
            }
        }
        return true;

    }
}
