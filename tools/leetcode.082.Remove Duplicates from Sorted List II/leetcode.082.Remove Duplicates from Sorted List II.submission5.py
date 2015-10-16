# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0x7fffffff)
        dummy.next= head
        p = dummy
        n = p.next
        nn = p.next.next
        while nn:
            cur = n.val
            flag = False
            while nn and nn.val == cur:
                flag = True
                nn = nn.next
            if flag:
                p.next = nn
                if not nn:
                    break
                n = nn
                nn = n.next
            else:
                p = n
                n = nn
                nn = nn.next
        return dummy.next
            