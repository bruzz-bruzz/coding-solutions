# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        res = []
        while head:
            if head.val != val:
                res.append(head.val)
            head = head.next
        if not res:
            return ListNode().next
        for x in range(len(res)):
            res[x] = ListNode(res[x])
        for x in range(len(res) - 1):
            res[x].next = res[x+1]
        return res[0]