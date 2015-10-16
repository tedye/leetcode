# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head: return
        if not head.next: return
        
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        length = len(nodes)
        temp = [None] * length 
        if length%2:
            temp[::2] = nodes[:length//2+1]
            temp[1::2] = nodes[length//2+1:][::-1]
        else:
            temp[::2] = nodes[:length//2]
            temp[1::2] = nodes[length//2:][::-1]
        nodes = temp
        pos = 1
        while pos < length:
            nodes[pos-1].next = nodes[pos]
            pos += 1
        nodes[pos-1].next = None
    
        