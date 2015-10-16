# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        c = 0
        dummy = ListNode(None)
        temp = dummy
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s // 10
            s %= 10
            temp.next = ListNode(s)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + c
            c = s // 10
            s %= 10
            temp.next = ListNode(s)
            temp = temp.next
            l1 = l1.next
        while l2:
            s = l2.val + c
            c = s // 10
            s %= 10
            temp.next = ListNode(s)
            temp = temp.next
            l2 = l2.next 
        if c:
            temp.next = ListNode(c)
        return dummy.next
        