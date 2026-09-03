class ListNode():
    def __init__(self,value=0,prevNode=None,nextNode=None):
        self.value=value
        self.nextNode=nextNode
        self.prevNode=prevNode

class LRUCache:
    # so we need a hashmap, and then we also store a doubly linkedlist
    def __init__(self, capacity: int):
        self.hashmap={}
        self.nodeToKey={}
        self.capacity=capacity
        self.head=ListNode()
        self.tail=ListNode()
        self.head.nextNode=self.tail
        self.tail.prevNode=self.head

    # we check the hashmap right, if its not inside we return -1
    #if its inside we return it and then update the most recently used
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # Its inside
        curNode=self.hashmap[key]
        prevNode=curNode.prevNode
        nextNode=curNode.nextNode
        prevNode.nextNode=nextNode
        nextNode.prevNode=prevNode

        curNode.nextNode=self.head.nextNode
        self.head.nextNode.prevNode=curNode
        self.head.nextNode=curNode
        curNode.prevNode=self.head

        return curNode.value
    def put(self, key: int, value: int) -> None:
        #first we check if the key is in the hashmap, if it is, we need to update it, if it isnt, then we add it into the cache. if the cache is full, we need to evict.
        if key in self.hashmap:
            #update the node
            curNode=self.hashmap[key]
            curNode.value=value
            prevNode=curNode.prevNode
            nextNode=curNode.nextNode
            
            prevNode.nextNode=nextNode
            nextNode.prevNode=prevNode

            curNode.nextNode=self.head.nextNode
            self.head.nextNode.prevNode=curNode
            self.head.nextNode=curNode
            curNode.prevNode=self.head

        else:
            if len(self.hashmap)==self.capacity:
                #have to evict
                evictedNode=self.tail.prevNode
                self.tail.prevNode.prevNode.nextNode=self.tail
                self.tail.prevNode=self.tail.prevNode.prevNode
                # issue here is that we need to delete the value not the key     
                evictedKey=self.nodeToKey[evictedNode]
                self.hashmap.pop(evictedKey)
                self.nodeToKey.pop(evictedNode)
            
            newNode=ListNode(value=value)
            newNode.nextNode=self.head.nextNode
            self.head.nextNode.prevNode=newNode
            self.head.nextNode=newNode
            newNode.prevNode=self.head
            self.hashmap[key]=newNode
            self.nodeToKey[newNode]=key


        
