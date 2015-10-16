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
        if not head or not head.next: return head
        c = 0
        temp = head
        while temp:
            temp = temp.next
            c += 1
        
        k %= c
        if k == 0: return head
        temp = head
        i = 0
        while i < k:
            temp = temp.next
            i+= 1
        p = head
        while temp.next:
            p = p.next
            temp = temp.next
        
        x = p.next
        temp.next = head
        p.next = None
        return x
        