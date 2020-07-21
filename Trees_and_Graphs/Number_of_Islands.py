class Solution:
    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        """
        DFS
        Recursive

        logic
        - loop each node in the graph
        - first match '1' count island
        - recursive left, right, up and down
            - if continue '1', update to '0'

        time  O(M * N)
        space O(M * N)

        """
        if row < 0 or col < 0 \
                or row > len(grid) or col > len(grid[0]) \
                or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        # left
        if row != 0:
            self.dfs(grid, row - 1, col)
        # right
        if row != (len(grid) - 1):
            self.dfs(grid, row + 1, col)
        # up
        if col != 0:
            self.dfs(grid, row, col - 1)
        # down
        if col != (len(grid[0]) - 1):
            self.dfs(grid, row, col + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print(f'r {r}, c {c}, v: {grid[r][c]}, count {count}')
                if grid[r][c] == '1':
                    # print(f' >>> r {r}, c {c}, v: {grid[r][c]}, count {count}')
                    count += 1
                    self.dfs(grid, r, c)
        return count
