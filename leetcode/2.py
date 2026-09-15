# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = r = ''
        while l1:
            l += str(l1.val)
            l1 = l1.next
        while l2:
            r += str(l2.val)
            l2 = l2.next
        l = int(l[::-1])
        r = int(r[::-1])
        l += r
        l = str(l)[::-1]
        arr = [ListNode(int(l[0]))]
        for x in range(1,len(l)):  
            arr.append(ListNode(int(l[x])))
        for x in range(len(arr) - 1):
            arr[x].next = arr[x+1]
        return arr[0]