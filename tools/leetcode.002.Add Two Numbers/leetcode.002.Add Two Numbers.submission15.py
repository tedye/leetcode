# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        s = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        head = ListNode(s)
        temp = head
        while l1.next or l2.next:
            val1 = val2 = 0
            if l1.next:
                l1 = l1.next
                val1 = l1.val
            if l2.next:
                l2 = l2.next
                val2 = l2.val
            s = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            temp.next = ListNode(s)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return head
            
                