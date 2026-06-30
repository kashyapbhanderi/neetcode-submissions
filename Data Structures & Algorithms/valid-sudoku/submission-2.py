class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= [0] * 9
        cols= [0] * 9
        blocks= [0] * 9

        for r in range(0,9):
            for c in range(0,9):
                val=board[r][c]
                if val is ".":
                    continue

                bit = 1 << int(val)

                block_idx=(r//3)*3+(c//3)
                if (rows[r] & bit) or (cols[c] & bit) or (blocks[block_idx] & bit):
                    return False

                rows[r] |= bit
                cols[c] |= bit
                blocks[block_idx] |= bit
                
        return True         