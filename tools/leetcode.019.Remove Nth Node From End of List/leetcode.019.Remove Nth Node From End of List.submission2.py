# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    # @param {ListNode} head    # @param {integer} n    # @return {ListNode}    def removeNthFromEnd(self, head, n):        if not head: return None        dummy = ListNode(None)        dummy.next = head        first = head        for i in range(n):            first = first.next        second = dummy                while first!= None:            first = first.next            second = second.next                second.next = second.next.next        return dummy.next        