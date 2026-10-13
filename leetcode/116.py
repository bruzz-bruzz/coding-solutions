"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def bfs(r):
            q = deque([r])
            res = []
            if not r:
                return res
            while q:
                same = []
                for _ in range(len(q)):
                    p = q.popleft()
                    if p.left:
                        q.append(p.left)
                    if p.right:
                        q.append(p.right)
                    same.append(p)
                res.append(same)
            return res
        arr = bfs(root)
        if not arr:
            return root
        for x in range(len(arr)):
            for y in range(len(arr[x]) - 1):
                arr[x][y].next = arr[x][y + 1]
        return arr[0][0]