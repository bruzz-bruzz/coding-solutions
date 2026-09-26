# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def bfs(r):
            q = [r]
            res = []
            if not r:
                return res
            while q:
                same = []
                for _ in range(len(q)):
                    p = q.pop(0)
                    same.append(p.val)
                    if p.left:
                        q.append(p.left)
                    if p.right:
                        q.append(p.right)
                res.append(same)
            return res
        arr = bfs(root)
        res = []
        for x in arr:
            res.append(x[len(x) - 1])
        return res