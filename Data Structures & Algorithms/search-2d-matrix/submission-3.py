class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            mOne, mTwo = m // COLS, m % COLS

            if matrix[mOne][mTwo] > target:
                r = m - 1
            elif matrix[mOne][mTwo] < target:
                l = m + 1

            else:
                return True


        return False