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
        l = []
        while temp:
            d[temp] = RandomListNode(temp.label)
            l.append(d[temp])
            temp = temp.next
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        
        for n in d:
            if n:
                d[n].random = d[n.random]
        
        return d[head]
        