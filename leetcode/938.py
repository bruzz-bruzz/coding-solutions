# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        a = []
        def dfs(r):
            if not r:
                return
            if r.val >= low and r.val <= high:
                a.append(r.val)
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return sum(a)