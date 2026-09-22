# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        d = {}
        while head:
            d[head.val] = 1 + d.get(head.val,0)
            head = head.next
        k = list(d.keys())
        k.sort()
        res = []
        for x in k:
            if d[x] == 1:
                res.append(ListNode(x))
        if not res:
            return ListNode().next
        for x in range(len(res) - 1):
            res[x].next = res[x+1]
        return res[0]