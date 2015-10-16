# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head: return None
        if not head.next: return None
        
        a = set()
        temp = head
        while temp:
            if temp not in a:
                a.add(temp)
                temp = temp.next
            else:
                return temp
        return None
        