class LRUCache:
    class ListNode:
        def __init__(self,k,v):
            self.key = k
            self.val = v
            self.next = None
            self.prev = None
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = self.ListNode(None,None)
        self.tail = self.ListNode(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    # @return an integer
    def get(self, key):
        if key not in self.nodes:
            return -1
        self.touch(self.nodes[key])
        return self.nodes[key].val
    
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.nodes:
            self.nodes[key].val = value
            self.touch(self.nodes[key])
        else:
            if self.size == self.capacity:
                self.size -= 1
                node = self.tail.prev
                p = node.prev
                p.next =self.tail
                self.tail.prev = p
                del self.nodes[node.key]
            self.size += 1
            node = self.ListNode(key,value)
            temp = self.head.next
            self.head.next= node
            node.prev = self.head
            node.next = temp
            temp.prev = node
            self.nodes[key] = node
            
        
    def touch(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        
        
        