# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val <= head.next.val:
                return head
            else:
                temp= head.next
                temp.next = head
                head.next= None
                return temp
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        r = self.sortList(slow.next)
        slow.next = None
        l = self.sortList(head)
        
        dummy = ListNode(0)
        temp = dummy
        while r or l:
            if r and l:
                if r.val > l.val:
                    temp.next = l
                    temp = temp.next
                    l = l.next
                    temp.next = None
                else:
                    temp.next = r
                    temp = temp.next
                    r = r.next
                    temp.next = None
            elif r:
                temp.next = r
                break
            elif l:
                temp.next = l
                break
        return dummy.next
        
