# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        temp = head
        temp1 = head.next
        temp.next = None
        while temp1:
            n = temp1.next
            temp1.next = temp
            temp = temp1
            temp1 = n
        return temp
        