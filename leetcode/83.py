# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        arr = []
        while head:
            if head.val not in arr:
                arr.append(head.val)
            head = head.next
        if not arr:
            return ListNode().next
        arr.sort()
        for x in range(len(arr)):
            arr[x] = ListNode(arr[x])
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]