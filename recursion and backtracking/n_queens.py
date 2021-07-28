class Solution:
    def initialize(self, n):
        current_col = 0
        left_check = [0 for i in range(n)]
        upper_diag_check = [0 for i in range(2*n - 1)]
        lower_diag_check = [0 for i in range(2*n - 1)]
        row = [0 for i in range(n)]
        board = [row for i in range(n)]
        res = []

        def n_queens(current_col):
            nonlocal n, left_check, upper_diag_check, lower_diag_check, board, res 
            if current_col == n:
                self.res.append(board)
                return
            for row in range(0, n):
                if left_check[row] == 0 and upper_diag_check[row + current_col] == 0 and lower_diag_check[n - 1 + current_col - row] == 0:
                    left_check[row], upper_diag_check[row + current_col], lower_diag_check[n - 1 + current_col - row] = 1, 1, 1
                    board[row][current_col] = 1
                    if self.n_queens(current_col + 1, n, left_check[:], upper_diag_check[:], lower_diag_check[:], board[:]):
                        return True
                    board[row][current_col] = 0
                    left_check[row], upper_diag_check[row + current_col], lower_diag_check[n - 1 + current_col - row] = 0, 0, 0
    


        n_queens()
