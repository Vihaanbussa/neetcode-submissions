class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            rowset = set()
            colset = set()
            for col in range(len(board[row])):
                if board[row][col] not in rowset:
                    rowset.add(board[row][col])
                elif board[row][col] != '.':
                    print(rowset)
                    print(board[row][col])
                    return False
                if board[col][row] not in colset:
                    colset.add(board[col][row])
                elif board[col][row] != '.':
                    print(board[col][row])
                    print(colset)
                    return False
        for box in range(0, 9, 3):
            boxset = set()
            for row in range(box, box+3):
                for col in range(3):
                    if board[row][col] not in boxset:
                        boxset.add(board[row][col])
                    elif board[row][col] != '.':
                        return False
        for box in range(0, 9, 3):
            boxset = set()
            for row in range(box, box+3):
                for col in range(3,6):
                    if board[row][col] not in boxset:
                        boxset.add(board[row][col])
                    elif board[row][col] != '.':
                        return False
        for box in range(0, 9, 3):
            boxset = set()
            for row in range(box, box+3):
                for col in range(6,9):
                    if board[row][col] not in boxset:
                        boxset.add(board[row][col])
                    elif board[row][col] != '.':
                        return False

        print(rowset)
        print(colset)
        return True
