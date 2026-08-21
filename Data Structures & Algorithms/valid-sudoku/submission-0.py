class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        for z in range(9):

            col_offset = (z%3) * 3
            row_offset = (z//3) * 3
            square = set() 

            for rel_col in range(3):
                for rel_row in range(3):

                    item = board[rel_row + row_offset][rel_col + col_offset]
                    if item != ".":
                        if item in square or item in columns[rel_col + col_offset] or item in rows[rel_row + row_offset]:
                            return False
                        
                        square.add(item)
                        columns[rel_col + col_offset].add(item)
                        rows[rel_row + row_offset].add(item)


        return True
