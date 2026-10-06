# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        res = []
        def dfs(r,s):
            if r:
                s += r.val
                if s == targetSum and not r.left and not r.right:
                    res.append(True)
                dfs(r.left,s)
                dfs(r.right,s)
        dfs(root,0)
        return True in res