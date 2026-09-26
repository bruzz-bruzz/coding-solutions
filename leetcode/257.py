# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []
        def dfs(arr,r):
            tmp = arr[:]
            tmp += [str(r.val)]
            if not r.left and not r.right:
                res.append("->".join(tmp))
            else:
                if r.left:
                    dfs(tmp,r.left)
                if r.right:
                    dfs(tmp,r.right)
        dfs([],root)
        return res