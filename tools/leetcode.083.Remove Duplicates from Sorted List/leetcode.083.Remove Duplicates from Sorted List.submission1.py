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
        
        temp = head
        cur = temp.val
        while temp.next:
            if temp.next.val == cur:
                temp.next = temp.next.next
            else:
                temp = temp.next
                cur = temp.val
        return head
                