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
        d = {None:None}
        temp = head
        dummy = RandomListNode(0)
        dummy.next = head
        p = dummy
        while temp:
            p.next = RandomListNode(temp.label)
            d[temp] = p.next
            p = p.next
            temp = temp.next

        for n in d:
            if n:
                d[n].random = d[n.random]
        
        return d[head]
        