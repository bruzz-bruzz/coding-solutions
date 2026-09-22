# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = [root]
        res = []
        if not root:
            return res
        while q:
            same = []
            for _ in range(len(q)):
                p = q.pop(0)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                same.append(p.val)
            res.append(same)
        return res
            