# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        lists = [i for i in lists if i]
        if not lists: return None
        if len(lists) == 1: return lists[0]
        dummy = ListNode(0)
        d = dummy
        lists.sort(key=lambda x: x.val)
        while lists:
            temp = lists[0]
            d.next = temp
            temp = temp.next
            d = d.next
            d.next = None
            if temp:
                lists[0] = temp
                lists.sort(key=lambda x: x.val)
            else:
                lists = lists[1:]
        return dummy.next
        