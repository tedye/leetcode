# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        if not head.next: return False
        
        temp = head
        a = set()
        while temp:
            if temp not in a:
                a.add(temp)
                temp = temp.next
            else:
                return True
        return False
        