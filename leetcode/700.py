# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        q = [root]
        if not q:
            return None
        while q:
            for _ in range(len(q)):
                p = q.pop(0)
                if p.val == val:
                    return p
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return None