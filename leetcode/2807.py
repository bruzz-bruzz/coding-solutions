# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        gcd = []
        for x in range(len(arr) - 1):
            gcd.append(math.gcd(arr[x],arr[x+1]))
        tot = [ListNode(arr.pop(0))]
        while arr or gcd:
            if gcd:
                tot.append(ListNode(gcd.pop(0)))
            if arr:
                tot.append(ListNode(arr.pop(0)))
        for x in range(len(tot) - 1):
            tot[x].next = tot[x+1]
        return tot[0]