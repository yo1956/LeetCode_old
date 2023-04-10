from typing import Dict, List
#from collections import defaultdict
import collections
#from typing import list

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows = collections.defaultdict(set)
        #cols = collections.defaultdict(set)
        #square = collections.defaultdict(set)
        
        rows = dict(set)
        cols = dict(set)
        square = dict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if(    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in square[(r//3, c//3)]
                  ):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        
        return True

def main():
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    ans = sol.isValidSudoku(board)
    print(ans)
    
if __name__ == "__main__":
    main()