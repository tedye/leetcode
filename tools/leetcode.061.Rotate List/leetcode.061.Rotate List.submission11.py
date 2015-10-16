# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        k %= length
        if k == 0:
            return head
        
        temp1 = head
        p = length - k - 1
        while p > 0:
            temp1 = temp1.next
            p -= 1
        newhead = temp1.next
        temp1.next = None
        temp.next = head
        return newhead
        