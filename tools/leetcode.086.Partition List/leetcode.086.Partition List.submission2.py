# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head: return None
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        
        temp = head
        temp1 = dummy1
        temp2 = dummy2
        while temp:
            if temp.val < x:
                temp1.next = temp
                temp = temp.next
                temp1 = temp1.next
                temp1.next = None
            else:
                temp2.next = temp
                temp = temp.next
                temp2 = temp2.next
                temp2.next = None
        temp1.next = dummy2.next
        return dummy1.next
        