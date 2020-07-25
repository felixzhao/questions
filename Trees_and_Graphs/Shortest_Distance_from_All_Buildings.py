class Solution:
    def getPosition(self, row: int, col: int, width: int) -> int:
        return row * width + col

    def bfsLevelCount(self, grid: List[List[int]], start: [int], dist: dict, reached: dict) -> None:
        """
        BFS + visited
        level count

        logic:
        - a queue FIFO maintain iteration items
        - a dictionary 'visited' which maintains all items have been visited
        - for count each level
            - pop all items in one level at one time

        time  O(N), N is count of the node in graph which can be reached
        space O(N), N sames to above
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        queue = [start]
        visited = {}
        startKey = self.getPosition(start[0], start[1], colCount)
        visited[startKey] = 1
        level = 1
        while queue:
            for i in range(len(queue)):
                row, col = queue.pop(0)
                for rowOffset, colOffset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    newRow = row + rowOffset
                    newCol = col + colOffset
                    key = self.getPosition(newRow, newCol, colCount)
                    if 0 <= newRow < rowCount and 0 <= newCol < colCount \
                            and key not in visited \
                            and grid[newRow][newCol] != 1 \
                            and grid[newRow][newCol] != 2:
                        dist[key] = dist.get(key, 0) + level
                        reached[key] = reached.get(key, 0) + 1
                        visited[key] = visited.get(key, 0) + 1
                        queue.append([newRow, newCol])
            level += 1

    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS + visited
        (reached + distance)

        logic:
        - for each building find each empty land distance to this building
        - keep how many building can reach to this empty land
        - the empty land can reach all building with min distance is the result

        time  O(M^2*N^2)
        space O(M*N), O(2*M*N)

        """
        if not grid or len(grid) == 0:
            return -1
        buildingCount = sum(val for line in grid for val in line if val == 1)
        rows = len(grid)
        cols = len(grid[0])
        dist = {}
        reached = {}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.bfsLevelCount(grid, [r, c], dist, reached)
                    # print(f'row {r}, col {c}, {dist}')
                    # print(f' >>> reached {reached}')
        if not reached or not dist or max(reached.values()) < buildingCount:
            return -1
        else:
            minDistance = float('inf')
            for k, v in dist.items():
                if reached[k] == buildingCount:
                    minDistance = min(minDistance, v)
            return minDistance

