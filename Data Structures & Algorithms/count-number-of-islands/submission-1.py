class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows, cols = len(grid), len(grid[0])

        islands = 0

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                ro, co = q.popleft()
                for dr, dc in directions:
                    row, col = ro + dr, co + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
        


        


        