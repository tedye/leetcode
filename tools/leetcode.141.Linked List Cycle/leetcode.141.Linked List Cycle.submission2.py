# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        
        # modify the node as visited mark
        temp = head
        while temp:
            if temp.val == 0x7fffffff:
                return True
            else:
                temp.val = 0x7fffffff
            temp = temp.next
        return False
        