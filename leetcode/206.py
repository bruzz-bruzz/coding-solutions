# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        res = []
        while t:
            res.append(ListNode(t.val))
            t = t.next
        if not res:
            h = ListNode()
            return h.next
        res.reverse()
        for x in range(len(res) - 1):
            res[x].next = res[x+1]
        return res[0]