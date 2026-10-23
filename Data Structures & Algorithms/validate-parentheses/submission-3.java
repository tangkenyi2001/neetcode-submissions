class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack= new ArrayDeque<>();
        Map <Character,Character> keyValue= Map.of(')','(','}','{',']','[');
        char curChar;
        for (int i=0;i<s.length();i++){
            curChar=s.charAt(i);
            if (keyValue.containsKey(curChar)){
                if (stack.peek()!=keyValue.get(curChar)){
                    System.out.println(stack.peek());
                    System.out.println(keyValue.get(curChar));
                    return false;
                }
                else{
                    stack.pop();
                }
            }
            else{
                stack.push(curChar);
            }
        }
        ;
        if (stack.size()!=0){
            return false;
        }
        return true;
    }
}
