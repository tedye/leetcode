# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        temp = head
        while temp:
            tail = temp.next
            node = RandomListNode(temp.label)
            temp.next = node
            node.next = tail
            temp = tail
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp = head
        dummy = RandomListNode(0)
        t = dummy
        while temp:
            t.next = temp.next
            t = t.next
            temp.next = t.next
            temp = temp.next
        return dummy.next