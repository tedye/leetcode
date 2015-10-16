# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next: return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        temp = p.next
        while temp and temp.next:
            n = temp.next.next
            p.next = temp.next
            p.next.next = temp
            temp.next = n
            p = temp
            temp = n
        return dummy.next
            
            
            
        