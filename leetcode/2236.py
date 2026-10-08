# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        s = []
        def recur(r):
            if not r:
                return
            s.append(r.val)
            recur(r.left)
            recur(r.right)
        recur(root.left)
        recur(root.right)
        return sum(s) == root.val