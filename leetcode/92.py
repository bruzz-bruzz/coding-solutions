# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        left -= 1
        right -=1
        while left < right:
            [arr[left],arr[right]] = [arr[right],arr[left]]
            left += 1
            right -= 1
        if not arr:
            return ListNode().next
        for x in range(len(arr)):
            arr[x] = ListNode(arr[x])
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]