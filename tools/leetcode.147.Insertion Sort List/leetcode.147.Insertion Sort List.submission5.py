# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head: return None
        if not head.next: return head
        
        dummy = ListNode(None)
        dummy.next = head
        remain = head.next
        dummy.next.next = None
        last = dummy.next
        while remain:
            current = remain
            remain = remain.next
            current.next = None
            if current.val < last.val:
                temp = dummy
                while temp.next.val < current.val:
                    temp = temp.next
                x = temp.next
                temp.next = current
                current.next = x
            else:
                last.next = current
                last = last.next
        return dummy.next
        