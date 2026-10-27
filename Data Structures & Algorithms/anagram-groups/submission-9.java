class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // is there anyway to compare 2 string in 0(n) time and see if its the same.
        // can we store the freq array as a string?
        Map <String,List<String>> hashmap = new HashMap<>();

        for (String str : strs){
            int[] freqArr = new int[26];
            for (int i=0; i<str.length();i++){
                char curChar=str.charAt(i);
                freqArr[curChar-'a']+=1;
            }
            StringBuilder curString = new StringBuilder();
            for (int i=0;i<26;i++){
                curString.append(Integer.toString(freqArr[i]));
                curString.append('x');
            }
            // System.out.println(curString);
            String stringhash = curString.toString();
            // System.out.println(stringhash);
            hashmap.computeIfAbsent(stringhash,x->new ArrayList<String>()).add(str);
            // System.out.println(hashmap);
        }
        List<List<String>> res = new ArrayList<>();

        for (Map.Entry<String,List<String>> entry : hashmap.entrySet()){
            res.add(new ArrayList<>(entry.getValue()));
        }
        return res;

    }
}
