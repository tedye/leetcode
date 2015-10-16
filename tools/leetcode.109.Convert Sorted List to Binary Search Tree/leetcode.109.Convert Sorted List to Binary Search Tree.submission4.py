# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        return self.helper(head,None)
        
    def helper(self,head,tail):
        if not head: return None
        if head.next == tail: return TreeNode(head.val)
        if head.next.next == tail:
            t1 = TreeNode(head.val)
            t2 = TreeNode(head.next.val)
            t2.left = t1
            return t2
        
        mid = head
        last = head
        cnt = 0
        while last.next != tail:
            if cnt % 2 == 0:
                mid = mid.next
            last = last.next
            cnt += 1
        t2 = TreeNode(mid.val)
        t2.left = self.helper(head,mid)
        t2.right = self.helper(mid.next,tail)
        
        return t2
            