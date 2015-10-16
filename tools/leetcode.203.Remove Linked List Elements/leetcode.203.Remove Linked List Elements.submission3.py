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
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next != None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next