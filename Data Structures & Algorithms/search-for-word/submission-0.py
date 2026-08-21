class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        mem = set()
        found = 0
        def foundLetter_atIndex_givenPosition(i:int, x:int, y:int):
            if i == len(word) - 1:
                return True
            mem.add((x,y))
            print(mem)
            print(f"Found {word[i]} at ({x}, {y})")
            for delta_x in range(-1,2):
                for delta_y in range(-1,2):
                    if delta_x + delta_y == -1 or delta_x+delta_y == 1:
                        next_x = x+delta_x
                        next_y = y+delta_y
                        print(f"Looking for {word[i+1]} at ({next_x}, {next_y})")
                        if next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board[0]) and (next_x, next_y) not in mem and board[next_x][next_y] == word[i+1]:
                            result = foundLetter_atIndex_givenPosition(i + 1, next_x, next_y) 
                            if result:
                                return True
            
            mem.remove((x,y))
        
        for x in range(0,len(board)):
            for y in range(0,len(board[0])):
                if board[x][y] == word[0]:
                    result = foundLetter_atIndex_givenPosition(0, x, y)
                    if result:
                        return True
         
        return False





            