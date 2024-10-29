class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        start_col = [True] * num_rows
        goto_col = [False] * num_rows

        for col_idx in range(num_cols - 1):
            for row_idx in range(num_rows):

                if not start_col[row_idx]:
                    continue

                # TODO break if all goto_col true
                if row_idx > 0:
                    goto_col[row_idx - 1] |= grid[row_idx - 1][col_idx + 1] > grid[row_idx][col_idx]
                if row_idx + 1 < num_rows:
                    goto_col[row_idx + 1] |= grid[row_idx + 1][col_idx + 1] > grid[row_idx][col_idx]
                goto_col[row_idx] |= grid[row_idx][col_idx + 1] > grid[row_idx][col_idx]
            
            if not any(goto_col):
                return col_idx

            start_col = goto_col
            goto_col = [False] * num_rows

        else:
            return col_idx + 1 if any(start_col) else col_idx 