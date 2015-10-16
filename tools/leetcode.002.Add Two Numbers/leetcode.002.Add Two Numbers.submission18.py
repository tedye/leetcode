# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        result = []
        while l1 != None:
            result.append(l1.val)
            l1 = l1.next
        cnt = 0
        while l2 != None:
            if cnt <= len(result) - 1:
                result[cnt] += l2.val
            else:
                result.append(l2.val)
            l2 = l2.next
            cnt += 1
        
        for i in range(len(result)):
            if result[i] >= 10:
                result[i] %= 10
                if i == len(result) - 1: result.append(1)
                else:result[i+1] += 1
        link = None
        while result:
            temp = ListNode(result.pop())
            temp.next = link
            link = temp
        return link
            