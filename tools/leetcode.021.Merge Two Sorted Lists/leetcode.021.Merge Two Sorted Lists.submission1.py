# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        return dummy.next
                    