class ListNode{
    int val;
    ListNode next;
    ListNode(){
        this.val=0;
        this.next=null;
    }
    ListNode(int val){
        this.val=val;
        this.next=null;
    }
    }

class MyLinkedList {
    ListNode head;
    int size;
    public MyLinkedList() {
        this.head = new ListNode();
        this.size=0;


    }
    
    public int get(int index) {
        //
        ListNode temp = this.head;
        while (temp!=null){
            // System.out.println(temp.val);
            temp=temp.next;
        }
        // System.out.println("xxx");

        if (index>=this.size){
            return -1;
        }
        ListNode cur = this.head.next;
        for (int i=0;i<index;i++){
            cur=cur.next;
        }
        return cur.val;
    }
    
    public void addAtHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next=this.head.next;
        this.head.next=newNode;
        this.size++;

        ListNode temp = this.head;
        while (temp!=null){
            System.out.println(temp.val);
            temp=temp.next;
        }
        System.out.println("addAthead");
    }
    
    public void addAtTail(int val) {
        ListNode cur = this.head;
        while (cur!=null && cur.next!=null){
            cur=cur.next;
        }
        ListNode newNode = new ListNode(val);
        cur.next=newNode;
        this.size++;

        ListNode temp = this.head;
        while (temp!=null){
            System.out.println(temp.val);
            temp=temp.next;
        }
        System.out.println("addAtail");
    }
    
    public void addAtIndex(int index, int val) {
        if (index>this.size){
            return;
        }
        else if (index==this.size){
            ListNode cur = this.head;
            while (cur!=null && cur.next!=null){
                cur=cur.next;
            }
            ListNode newNode = new ListNode(val);
            cur.next=newNode;
            this.size++;
        }
        else{
            ListNode cur = this.head;
            
            for (int i=0;i<index;i++){
                cur=cur.next;
            }
            ListNode newNode = new ListNode(val);
            newNode.next=cur.next;
            cur.next=newNode;
            this.size++;
        }

        ListNode temp = this.head;
        while (temp!=null){
            System.out.println(temp.val);
            temp=temp.next;
        }
        System.out.println("addAtidx");
    }
    
    public void deleteAtIndex(int index) {
        if (index>=this.size){
            return;
        }
        else{
            ListNode cur = this.head;
            for (int i=0;i<index-1;i++){
                cur=cur.next;
            }
            cur.next=cur.next.next;
            this.size--;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */