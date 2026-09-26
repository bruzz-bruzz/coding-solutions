class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(pos):
            x,y = pos[0],pos[1]
            if grid[x][y] == '1':
                grid[x][y] = '0'
                if x < len(grid) - 1:
                    recur([x + 1,y])
                if x > 0:
                    recur([x - 1,y])
                if y < len(grid[0]) - 1:
                    recur([x,y + 1])
                if y > 0:
                    recur([x,y - 1])
        c = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1':
                    c += 1
                    recur([x,y])
        return c