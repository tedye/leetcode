# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        temp = head
        cur = temp.val
        while temp.next:
            if temp.next.val == cur:
                temp.next = temp.next.next
            else:
                cur = temp.next.val
                temp = temp.next
        return head
            