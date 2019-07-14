class Solution:
    def __init__(self):
        self.n = 0

    def maxAreaOfIsland(self, grid):

        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    self.n = 0
                    self.dfs(grid, i, j)

                    maximum = max(maximum, self.n)

        return maximum

    def dfs(self, grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return

        self.n += 1
        grid[i][j] = 0
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
sol = Solution()
rst = sol.maxAreaOfIsland(grid)
print(rst)
