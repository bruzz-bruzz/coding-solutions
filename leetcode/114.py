# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        arr = []
        def dfs(r):
            if not r:
                return
            arr.append(r.val)
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        arr.pop(0)
        root.left = None
        d = root
        while arr:
            p = arr.pop(0)
            d.right = TreeNode(p)
            d = d.right
        return root