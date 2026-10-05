class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]


        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    ro = row + dr
                    co = col + dc
                    if (ro, co) not in visited and ro in range(rows) and co in range(cols) and grid[ro][co] == "1":
                        queue.append((ro, co))
                        visited.add((ro, co))
                        


        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    numIslands += 1


        return numIslands

        


        


        