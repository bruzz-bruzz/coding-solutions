# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = deque([root])
        res = []
        if not root:
            return res
        rev = False
        while q:
            same = []
            for _ in range(len(q)):
                p = q.popleft()
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
                same.append(p.val)
            if rev:
                same = same[::-1]
            rev = not rev
            res.append(same)
        return res