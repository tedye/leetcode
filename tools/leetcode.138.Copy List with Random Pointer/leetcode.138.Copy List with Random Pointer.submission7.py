# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        d = {}
        temp = head
        while temp:
            node = RandomListNode(temp.label)
            d[temp] = node
            temp = temp.next
        
        for node in d:
            if node.next:
                d[node].next = d[node.next]
            if node.random:
                d[node].random = d[node.random]
        return d[head]
        