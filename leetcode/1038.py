# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        k = []
        d = {}
        def dfs(r):
            if not r:
                return
            k.append(r.val)
            d[r.val] = r
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        k.sort()
        s = sum(k)
        while k:
            p = k.pop(0)
            d[p].val = s
            s -= p
        return root