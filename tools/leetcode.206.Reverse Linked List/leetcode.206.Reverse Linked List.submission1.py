# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        wkset = [None, head, head.next]
        
        while wkset[2]:
            wkset[1].next = wkset[0]
            wkset[0] = wkset[1]
            wkset[1] = wkset[2]
            wkset[2] = wkset[2].next
        wkset[1].next = wkset[0]
        return wkset[1]
        