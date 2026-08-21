class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 
        columns = [0] * 9
        for z in range(9):

            col_offset = (z%3) * 3
            row_offset = (z//3) * 3
            square = 0

            for rel_col in range(3):
                for rel_row in range(3):

                    item = board[rel_row + row_offset][rel_col + col_offset]
                    if item != ".":
                        item = 1 << int(item)-1
                        if item & square or item & columns[rel_col + col_offset] or item & rows[rel_row + row_offset]:
                            return False
                        
                        square |= (item)
                        columns[rel_col + col_offset] |= (item)
                        rows[rel_row + row_offset] |= (item)


        return True
