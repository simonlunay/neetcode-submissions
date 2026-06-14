class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0

        rows, cols = len(grid), len(grid[0])

        visited = set()

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


        

        def bfs(r, c):
            area = 1
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        area += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return area
                




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))




        return maxArea
        