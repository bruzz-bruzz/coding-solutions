# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        arr = []
        while head:
            arr.append(ListNode(head.val))
            head = head.next
        if not arr:
            return ListNode().next
        t = k % len(arr)
        while t > 0:
            arr.insert(0,arr.pop())
            t -= 1
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]