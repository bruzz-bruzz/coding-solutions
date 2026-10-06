# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res = []
        def recur(r,s):
            if r:
                s += str(r.val)
                if not r.left and not r.right:
                    res.append(s)
                recur(r.left,s)
                recur(r.right,s)
        recur(root,'')
        c = 0
        for x in res:
            c += int(x)
        return c