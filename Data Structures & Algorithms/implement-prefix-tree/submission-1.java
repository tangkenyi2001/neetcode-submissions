class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean endOfWord=false;
}
class PrefixTree {
    private TrieNode root;

    public PrefixTree() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur=root;
        for (int j=0;j<word.length();j++){
            int i=word.charAt(j)-'a';
            if (cur.children[i]==null){
                cur.children[i]=new TrieNode();
            }
            cur=cur.children[i];

        }
        cur.endOfWord=true;
    }

    public boolean search(String word) {
        TrieNode cur=root;
        for (int j=0;j<word.length();j++){
            int i = word.charAt(j)-'a';
            if (cur.children[i]==null){
                return false;
            }
            else{
                System.out.println(word.charAt(j));
                cur=cur.children[i];
            }
        }
        if (!cur.endOfWord){
            return false;
        }
        return true;
    }

    public boolean startsWith(String prefix) {
        TrieNode cur=root;
        for (int j=0;j<prefix.length();j++){
            int i = prefix.charAt(j)-'a';
            if (cur.children[i]==null){
                return false;
            }
            else{
                cur=cur.children[i];
            }
        }
        return true;
    }
}
