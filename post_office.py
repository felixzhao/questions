
def shortestDistanceToPostOffice(grid):
	"""
    x  x  x  x  x 
    2  1  2  x  x 
    1  0  1  x  x 
    2  1  1  0  1   
    x  x  1  1  2 

    A grid which width equal to height.
    existed one or more office site in the grid ( figure out as 0 )
    rest other cells are normal houses (fiout out as X)
    try to find shortest distance from each house to closest office.
    
	time complexity: O(P * V * E) , P is office count, V is cell in grid, E is connect between each cell
	space complexity: O(V)

	"""
	width = len(grid)
	PostOfficePlaces = []
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 0:
				PostOfficePlaces.append((i, j))
	for startPlace in PostOfficePlaces:
		queue = []
		visited = []
		queue.append(startPlace)
		for place in PostOfficePlaces:
			visited.append(place)
		while queue:
			p = queue.pop(0)
			x, y = p
			# left
			if x > 0:
				if grid[x - 1][y] not in visited and grid[x - 1][y] > grid[x][y] + 1:
					grid[x - 1][y] = grid[x][y] + 1
					queue.append((x - 1, y))
					visited.append((x - 1, y))
			# right
			if x < width - 1:
				if grid[x + 1][y] not in visited and grid[x + 1][y] > grid[x][y] + 1:
					grid[x + 1][y] = grid[x][y] + 1
					queue.append((x + 1, y))
					visited.append((x + 1, y))
			# up
			if y > 0:
				q = grid[x][y - 1]
				if q not in visited and q > grid[x][y] + 1:
					grid[x][y - 1] = grid[x][y] + 1
					queue.append((x, y - 1))
					visited.append((x, y - 1))
			# down
			if y < width - 1:
				q = grid[x][y + 1]
				if q not in visited and q > grid[x][y] + 1:
					grid[x][y + 1] = grid[x][y] + 1
					queue.append((x, y + 1))
					visited.append((x, y + 1))