class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.pre=self.head

        self.hashset={}
        self.capacity=capacity        

    def get(self, key: int) -> int:
        if key in self.hashset:
            node = self.hashset[key]
            prev=node.pre
            post=node.next
            prev.next=post
            post.pre=prev

            prev=self.tail.pre
            prev.next=node
            node.pre=prev
            node.next=self.tail
            self.tail.pre=node
            
            return self.hashset[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashset:
            node = self.hashset[key]
            node.val = value   # update value

            # remove from current position
            node.pre.next = node.next
            node.next.pre = node.pre
        else:
            if len(self.hashset) >= self.capacity:
                # evict least recently used (head.next)
                removed = self.head.next
                self.head.next = removed.next
                removed.next.pre = self.head
                del self.hashset[removed.key]

            node = Node(key, value)
            self.hashset[key] = node

        # insert at tail (most recently used)
        tailprev = self.tail.pre
        tailprev.next = node
        node.pre = tailprev
        node.next = self.tail
        self.tail.pre = node