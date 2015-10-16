# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # use hashtable
        if not head:
            return False
        d = set()
        temp = head
        while temp:
            if temp not in d:
                d.add(temp)
            else:
                return True
            temp = temp.next
        return False
        