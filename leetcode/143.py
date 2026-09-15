# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dum = head
        arr = []
        while dum:
            arr.append(dum.val)
            dum = dum.next
        ord = []
        while arr:
            if arr:
                ord.append(arr.pop(0))
            if arr:
                ord.append(arr.pop())
        dum = head
        while dum:
            dum.val = ord.pop(0)
            dum = dum.next
        return head