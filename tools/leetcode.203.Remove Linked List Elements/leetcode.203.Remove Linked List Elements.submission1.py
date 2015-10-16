# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return None
        dummy = ListNode(val-1)
        dummy.next = head
        wkset = [dummy, head]
        while wkset[1]:
            if wkset[1].val == val:
                wkset[1] = wkset[1].next
            else:
                wkset[0].next= wkset[1]
                wkset[0] = wkset[1]
                wkset[1] = wkset[1].next
        wkset[0].next = wkset[1]
        return dummy.next