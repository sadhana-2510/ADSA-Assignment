def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if no queen can attack this position horizontally
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower-left diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(board, col):
        if col == n:
            solutions.append([''.join(row) for row in board])
            return
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'  # Backtrack
                
    solutions = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(empty_board, 0)
    
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print("\n")

# Example usage:
N = 4
solutions = solve_n_queens(N)
print_solutions(solutions)
