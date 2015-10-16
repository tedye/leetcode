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
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1 and l2:
                sum = l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val+carry
                l1 = l1.next
            elif l2:
                sum = l2.val+carry
                l2 = l2.next
            elif carry:
                sum = carry
            carry = sum // 10
            sum = sum % 10
            temp.next = ListNode(sum)
            temp = temp.next
        return dummy.next
                