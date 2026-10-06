# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        def dfs(r,arr,s):
            if r:
                s += r.val
                if not r.left and not r.right and s == targetSum:
                    res.append(arr + [r.val])
                dfs(r.left,arr + [r.val],s)
                dfs(r.right,arr + [r.val],s)
        dfs(root,[],0)
        return res