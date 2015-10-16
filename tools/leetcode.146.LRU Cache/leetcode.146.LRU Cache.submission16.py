class LRUCache:
    class Node:
        def __init__(self,key,value):
            self.val = value
            self.key = key
            self.next = None
            self.prev = None
    
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.d = {}
        self.head = self.Node(None,None)
        self.tail = self.Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # @return an integer
    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.touch(node)
            return node.val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.d:
            node = self.d[key]
            self.touch(node)
            node.val = value
        else:
            if self.count == self.capacity:
                node = self.tail.prev
                p = node.prev
                p.next = self.tail
                self.tail.prev = p
                del self.d[node.key]
                self.count -= 1
            self.count += 1
            n = self.head.next
            node = self.Node(key,value)
            self.head.next = node
            node.prev = self.head
            node.next = n
            n.prev = node
            self.d[key] = node
    
    def touch(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
        n = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = n
        n.prev = node
            
            
        
        