# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for x in lists:
            while x:
                arr.append(x.val)
                x = x.next
        arr.sort()
        if not arr:
            return ListNode().next
        for x in range(len(arr)):
            arr[x] = ListNode(arr[x])
        for x in range(len(arr) -1 ):
            arr[x].next = arr[x+1]
        return arr[0]