# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        arr = []
        def dfs(r):
            if not r:
                return
            dfs(r.left)
            arr.append(TreeNode(r.val))
            dfs(r.right)
        dfs(root)
        for x in range(len(arr) - 1):
            arr[x].right = arr[x+1]
        r = TreeNode(-1)
        r.right = arr[0]
        self.r = r
    def next(self) -> int:
        self.r = self.r.right
        return self.r.val

    def hasNext(self) -> bool:
        return True if self.r.right else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()