# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head: return None
        
        i = 1
        temp = head
        while temp.next != None:
            i += 1
            temp = temp.next
        temp.next = head

        k = k % i
        if k == 0:
            temp.next = None
            return head

        temp1 = temp
        jump = i - k
        while jump > 0:
            temp1 = temp1.next
            jump -= 1
        t = temp1.next
        temp1.next = None

        return t
        