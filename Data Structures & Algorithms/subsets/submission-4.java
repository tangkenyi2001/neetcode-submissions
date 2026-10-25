class Solution {
    List<List<Integer>> res;
    List<Integer> path;
    public void backtrack(int index,int[] nums){
        if (index==nums.length){
            this.res.add(new ArrayList<>(path));
            return;
        }
        this.path.add(nums[index]);
        backtrack(index+1,nums);
        this.path.remove(this.path.size()-1);
        backtrack(index+1,nums);
    }
    public List<List<Integer>> subsets(int[] nums) {
        this.res = new ArrayList<>();
        this.path = new ArrayList<>();

        backtrack(0,nums);
        return this.res;
    }
}
