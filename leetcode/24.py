# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        if not arr:
            return ListNode().next
        l,r = 0,1
        while r < len(arr):
            arr[l],arr[r] = arr[r],arr[l]
            l += 2
            r += 2
        for x in range(len(arr)):
            arr[x] = ListNode(arr[x])
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]