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
        if not head: return None
        d = dict()
        temp = head
        d[temp] = RandomListNode(temp.label)
        while temp.next != None:
            d[temp.next] = RandomListNode(temp.next.label)
            d[temp].next = d[temp.next]
            temp = temp.next
        temp = head
        if temp.random != None:
            d[temp].random = d[temp.random] 
        while temp.next != None:
            temp = temp.next
            if temp.random != None:
                d[temp].random = d[temp.random]
        
        return d[head]
            
                    