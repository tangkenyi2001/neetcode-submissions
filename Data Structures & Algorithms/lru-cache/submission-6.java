class ListNode{
    int val;
    int key;
    ListNode next;
    ListNode prev;
    ListNode(int key,int val){
        this.val=val;
        this.key=key;
        this.next=null;
        this.prev=null;
    }
}

class LRUCache {
    int capacity;
    ListNode head;
    ListNode tail;
    Map<Integer,ListNode> hashmap;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        this.head=new ListNode(0,0);
        this.tail=new ListNode(0,0);
        this.hashmap= new HashMap<>();
        this.tail.prev=this.head;
        this.head.next=this.tail;

    }
    public void moveNodeToTail(ListNode curNode){
        ListNode prevNode = curNode.prev;
        ListNode nextNode = curNode.next;
        prevNode.next=nextNode;
        nextNode.prev=prevNode;
        ListNode secondLastNode=this.tail.prev;
        secondLastNode.next=curNode;
        curNode.prev=secondLastNode;
        curNode.next=this.tail;
        this.tail.prev=curNode;
    }
    public int get(int key) {
        // We first check the item if its in the hashmap, if not, we return -1
        // If it is in the hashmap, we have to update the node to the tail
        if (!this.hashmap.containsKey(key)){
            return -1;
        }
        else{
            ListNode curNode = this.hashmap.get(key);
            moveNodeToTail(curNode);
            return this.hashmap.get(key).val;
        }
    }
    
    public void addKeyValue(int key, int value){
        ListNode curNode=new ListNode(key,value);
        this.hashmap.put(key,curNode);
        ListNode secondLastNode=this.tail.prev;
        secondLastNode.next=curNode;
        curNode.prev=secondLastNode;
        curNode.next=this.tail;
        this.tail.prev=curNode;
    }
    public void put(int key, int value) {
        // if it is already in cache, we update value and move it to most recent
        if (this.hashmap.containsKey(key)){
            ListNode curNode = this.hashmap.get(key);
            curNode.val=value;
            moveNodeToTail(curNode);
        }
        //if its not in cache, we check capacity, if under just add in, if over capcacity, we need to evict
        else{
            if (this.hashmap.size()<this.capacity){
                addKeyValue(key,value);

            }
            else{
                //Skip the first node
                ListNode evictedNode = this.head.next;
                ListNode secondNode = this.head.next.next;
                this.head.next=secondNode;
                secondNode.prev=this.head;
                this.hashmap.remove(evictedNode.key);
                addKeyValue(key,value);

            }
        }
    }
}
